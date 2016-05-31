import json

from flask_restful import Resource, reqparse
import traceback


def needs_token(post_function):
    """Simple decorator that's supposed to be used on handler post functions requiring a token"""
    def wrapper(*args, **kwargs):
        # TODO : implement the user checking
        return post_function(*args, **kwargs)
    return wrapper


class BaseHandler(Resource):
    """This is the base abstract handler, instantiates a request parser,
    and simplifies a couple of operations"""

    def __init__(self):
        """The constructor for this abstract class just creates a request_parser"""
        super().__init__()
        self.reqparse = reqparse.RequestParser()
        self.args = None

    def do_request_parsing(self):
        self.args = self.reqparse.parse_args()

    def get(self):
        return {"status": "Correc'"}


class BaseDataHandler(BaseHandler):
    def __init__(self):
        """The constructor for this abstract class just creates a request_parser"""
        super().__init__()
        self.reqparse.add_argument("data", required=True, type=str)

    def do_request_parsing(self):
        super().do_request_parsing()
        self.json_data = json.loads(self.args["data"])


class ErrorCatcher:
    """Error-catching decorator, used to decorate the API handler's post functions"""

    # this lists the errors that are actually relevant to the user. Other errors are categorized are
    # "Internal errors" in the report
    SUPPORTED_ERRORS_TYPE = []

    def __init__(self, post_function):
        self.post = post_function

    def _is_supported_error_type(self, error_type):
        """Goes through the error types to see if it's a subclass (or an instance) of one of them"""
        for type in error_type:
            if issubclass(error_type, type):
                return self.SUPPORTED_ERRORS_TYPE.index(error_type)

    def __get__(self, obj, objtype):
        """Support for methods of a class's instance decoration"""
        import functools
        return functools.partial(self.__call__, obj)

    def __call__(self, *args, **kwargs):

        try:
            return self.post(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            return {"ERROR_CODE" : 0,
                    "MESSAGE" : "Internal error : " + str(e)}
