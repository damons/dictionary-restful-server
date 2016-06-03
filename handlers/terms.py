from .base import BaseHandler, IEMLRequiredHandler, BaseDataHandler


class BaseTermDataHandler(BaseHandler):
    """Base handlers for all request that send an IEML term's data for deleting or updating"""

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
        # first we need to check what's being changed
        # same_ieml = is the old ieml == new ieml
        # same_paradigm = old paradigm flag == new paradigm flag

        # if not(same_ieml and same_paradigm) we delete the relations for the old IEML

        # then we update the term's document

        # if not(same_ieml and same_paradigm), we update the relations and
        pass


class RemoveIEMLTermHandler(BaseHandler):

    def post(self, term_id):
        pass


class GetAllIEMLTermsHandler(BaseHandler):

    def post(self):
        return self.terms_db.get_all_terms()