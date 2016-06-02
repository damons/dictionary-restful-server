from .base import BaseHandler, IEMLRequiredHandler, BaseDataHandler


class BaseTermDataHandler(BaseHandler):

    def __init__(self):
        super().__init__()
        for field in ["IEML", "FR", "EN", "CANONICAL", "LAYER", "CLASS", "TAILLE", "CANONICAL"]:
            self.reqparse.add_argument(field, type=str, location="json")


class NewIEMLTermHandler(BaseTermDataHandler):

    def post(self):
        self.do_request_parsing()
        # TODO : implement the term saving


class UpdateIEMLTermHandler(BaseTermDataHandler):

    def post(self):
        pass


class RemoveIEMLTermHandler(BaseHandler):

    def post(self, term_id):
        pass


class GetAllIEMLTermsHandler(BaseHandler):

    def post(self):
        return self.terms_db.get_all_terms()