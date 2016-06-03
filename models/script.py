from models.base_queries import DBConnector
from requests import post
from json import loads
from urllib.parse import quote
from models.constants import PARSER_URL, PARSE_SCRIPT, GET_TABLES, RELATIONS
from models.exceptions import InvalidScript, NotAParadigm, InvalidDbState
from pymongo.errors import DuplicateKeyError


class ScriptQueries(DBConnector):

    def get_script(self, ieml):
        return self.scripts.find({"_id" : ieml})

    def save_term(self, ieml, tags):
        """Save a term to the database"""
        if self.get_script(ieml) is None:
            # save the paradigm
            self.save_table(ieml)

        self.terms.insert({
            "_id": ieml,
            "TAGS": {
                "FR": tags['FR'],
                "EN": tags['EN']
            }
        })

    def add_relation(self, relation, source, target):
        """ Add the relation to the source, and the anti-relation to the target."""
        self.scripts.update({'_id': source},
                            {'$push': {'RELATIONS': {
                                'TYPE': relation,
                                'TARGET': target
                            }}})

        self.scripts.update({'_id': target},
                            {'$push': {'RELATIONS': {
                                'TYPE': RELATIONS[relation],
                                'TARGET': source
                            }}})

    def save_table(self, ieml, paradigm=None, containing_tables=None):
        """Insert a table or paradigm into the database.
            if paradigm is set, insert a table otherwise insert a paradigm.
            The paradigm parameter is the containing paradigm.
            The containing_tables parameter is the tables containing this table (None in the case of paradigm)

            Database structure :
            {
                '_id': ieml of the element (index)
                'TYPE': 'PARADIGM' | 'TABLE' | 'CELL'
                'RELATIONS': [{ 'TARGET': ieml of the relation target,
                                 'TYPE': type of the relation (see constant.py)}, ...]
                'PARADIGM': ieml of the containing paradigm (if TYPE == CELL || TYPE == TABLE)
                'TABLES': [ieml of the containing tables] (if TYPE == CELL || TYPE == TABLE)
            }
            """
        script = self._get_script_from_parser(ieml)
        if script['taille'] == 1:
            raise NotAParadigm()

        insert = {
            '_id': ieml,
            'TYPE': 'PARADIGM' if paradigm is None else 'TABLE',
            'RELATIONS': []
        }

        if paradigm is not None:
            insert['PARADIGM'] = paradigm
            insert['TABLES'] = containing_tables
        else:
            containing_tables = []

        try:
            self.scripts.insert(insert)
        except DuplicateKeyError:
            # check if identical to inserted
            if self.scripts.find(insert) is None:
                raise InvalidDbState()

        tables, cells = self._get_tables_from_parser(ieml)
        for cell in cells:
            self._save_cell(cell, paradigm if paradigm is not None else ieml, ieml)
            # self.add_relation('CONTAINS', cell, ieml)

        containing_tables.append(ieml)
        for table in tables:
            self.save_table(table, paradigm=ieml, containing_tables=containing_tables)
            # self.add_relation('CONTAINS', table, ieml)

        # TODO add relations

    def _save_cell(self, ieml, paradigm, table):
        """
        Add the cell to the database. If already present, update the TABLES attribute with the table parameter.
        To add all the containing tables of a cell, you have to make multiple call of this method
        :param ieml: the ieml of the cell
        :param paradigm: the containing paradigm
        :param table: the containing table
        :return:
        """
        insertion = {
            '_id': ieml,
            'TYPE': 'CELL',
            'RELATIONS': [],
            'PARADIGM': paradigm,
            'TABLES': [table]
        }
        try:
            self.scripts.insert(insertion)
        except DuplicateKeyError:
            # Update the table list
            self.scripts.update({'_id': ieml}, {'$push': {'TABLES': table}})


    def _get_tables_from_parser(self, ieml):
        print("Request the parser for tables : " + ieml, end=" ---- ")
        response = post(PARSER_URL + GET_TABLES, data="iemltext=" + quote(ieml))
        if not response.ok:
            raise InvalidScript()
        print("ok")

        json = loads(response.text)
        if not json['success']:
            raise InvalidScript()

        tables = []
        cells = []

        for table in json['tree']['Tables']:
            for z in table['table']:
                for elem in z['slice']:
                    if elem['background'] == 'blue' or (elem['background'] == 'green' and elem['value'] != ieml):
                        # table
                        tables.append(elem['value'])
                    elif elem['background'] == 'gray' and len(elem['value']) != 0:
                        # cell
                        cells.append(elem['value'])

        return tables, cells

    def _get_script_from_parser(self, ieml):
        """
            Return a dict of the shape :
            {
                level : int,
                taille : int,
                class : int,
                success : boolean,
                canonical : [string]
            }
        :param ieml:
        :return:
        """
        print("Request the parser for script : " + ieml, end=' ---- ')
        response = post(PARSER_URL, data="iemltext=" + quote(ieml))
        if not response.ok:
            raise InvalidScript()
        print("ok")

        script = loads(response.text)
        if script['success']:
            return script
        else:
            raise InvalidScript()

if __name__ == '__main__':
    db = ScriptQueries()
    db.save_table("M:.-',M:.-',S:.-'B:.-'n.-S:.U:.-',_")