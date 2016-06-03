from models.constants import RELATIONS_COLLECTION
from .base_queries import DBConnector

class RelationsQueries(DBConnector):

    def __init__(self):
        super().__init__()
        self.relations = self.db_term[RELATIONS_COLLECTION]

    def delete_relations_for_term(self, term_id):
        pass

    def update_relations_for_term(self, term_id):
        pass