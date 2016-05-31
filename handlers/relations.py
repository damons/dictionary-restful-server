from .base import BaseHandler, IEMLRequiredHandler

"""Handlers dedicated to relations"""


class GetRelationsHandler(IEMLRequiredHandler):

    def post(self):
        pass


class GetRelationVisibilityHandler(IEMLRequiredHandler):

    def post(self):
        self.do_request_parsing()


class AddRelationVisibilityHandler(IEMLRequiredHandler):

    def post(self):
        self.reqparse.add_argument("stuff", required=True, type=str)
        self.do_request_parsing()


class RemoveRelationVisibility(IEMLRequiredHandler):

    def post(self):
        self.reqparse.add_argument("stuff", required=True, type=str)
        self.do_request_parsing()


class ToggleRelationVisibilityHandler(BaseHandler):

    def post(self):
        self.reqparse.add_argument("itemids", required=True, type=str)
        self.do_request_parsing()
