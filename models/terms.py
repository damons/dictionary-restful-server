from .base_queries import DBConnector

class TermsQueries(DBConnector):

    def get_all_terms(self):
        """Returns all the terms contained in the DB"""
        pass

    def new_ieml_term(self, **kwargs):
        raise NotImplemented()

    def search_by_tag(self, language):
        raise NotImplemented()

    def search_by_ieml(self, ieml):
        raise NotImplemented()