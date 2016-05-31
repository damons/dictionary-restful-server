"""All handlers in charge of annotations (tags)"""
from .base import BaseHandler


class GetAnnotationsHandler(BaseHandler):

    def post(self):
        self.reqparse.add_argument("ieml", required=True, type=str)
        pass


class RemoveAnnotationsHandler(BaseHandler):

    def post(self):
        self.reqparse.add_argument("_id", required=True, type=str)
        pass


class AddAnnotationHandler(BaseHandler):

    def post(self):
        self.reqparse.add_argument("ieml", required=True, type=str)
        self.reqparse.add_argument("annotation", required=True, type=str)
        pass


