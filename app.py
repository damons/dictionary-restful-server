from flask import Flask
from flask_restful import Api

from handlers import *

app = Flask(__name__)
api = Api(app)


### This is the api's routing table

# Search endpoint
api.add_resource(BaseHandler, '/api/hello')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0") # served on the local network