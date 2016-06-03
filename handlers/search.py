from .base import BaseHandler


class BaseSearchTermsHandler(BaseHandler):
    pass


class SearchENHandler(BaseSearchTermsHandler):

    def post(self, term_ieml):
        """Returns a list of the IEML terms matching the IEML string. Expected to basically just return at most one
        element"""
        return self.terms_db.search_by_ieml(term_ieml)


class SearchFRHandler(BaseSearchTermsHandler):

    def post(self, term_fr):
        """Returns a list of the IEML terms matching the input FR tag. Expected to basically just return at most one
        element"""
        return self.terms_db.search_by_tag(term_fr, "FR")


class SearchIEMLHandler(BaseSearchTermsHandler):

    def post(self, term_en):
        """Returns a list of the IEML terms matching the input EN tag. Expected to basically just return at most one
            element"""
        return self.terms_db.search_by_tag(term_en, "EN")
