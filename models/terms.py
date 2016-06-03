from .base_queries import DBConnector

class TermsQueries(DBConnector):

    def get_all_terms(self):
        """Returns all the terms contained in the DB"""
        return list(self.terms.find())

    def new_ieml_term(self, **kwargs):
        raise NotImplemented()

    def search_by_tag(self,tag, language):
        raise NotImplemented()

    def search_by_ieml(self, ieml):
        raise NotImplemented()

    def remove_term(self, term_id):
        pass