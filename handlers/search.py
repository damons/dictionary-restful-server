from .base import BaseHandler


class BaseSearchTermsHandler(BaseHandler):
    pass


class SearchENHandler(BaseSearchTermsHandler):

    def post(self, term_id):
        pass


class SearchFRHandler(BaseSearchTermsHandler):

    def post(self, term_id):
        pass


class SearchIEMLHandler(BaseSearchTermsHandler):

    def post(self, term_id):
        pass
