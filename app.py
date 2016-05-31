from flask import Flask
from flask_restful import Api

from handlers import *

app = Flask(__name__)
api = Api(app)


### This is the api's routing table ###

# Get all the IEML terms
api.add_resource(BaseHandler, '/api/allieml');

# Get an accesss token to the client
api.add_resource(BaseHandler, '/client/authenticate')

### Annotation editing endpoints
api.add_resource(BaseHandler, '/api/getannotations')
api.add_resource(BaseHandler, '/api/removeannotation')
api.add_resource(BaseHandler, '/api/addannotation')

### Relations editing and listing endpoints
api.add_resource(BaseHandler, '/api/getRelVisibility')
api.add_resource(BaseHandler, '/api/addRelVisibility') # requires login
api.add_resource(BaseHandler, '/api/remRelVisibility') # requires login
api.add_resource(BaseHandler, '/api/toggleRelVisibility')
api.add_resource(BaseHandler, '/api/rels')

### IEML edition endpoints
api.add_resource(BaseHandler, '/api/newieml') # requires login
api.add_resource(BaseHandler, '/api/updateieml') # requires login
api.add_resource(BaseHandler, '/api/remieml/:id') # requires login
api.add_resource(BaseHandler, '/api/exists/ieml/:id')
api.add_resource(BaseHandler, '/api/exists/FR/:id')
api.add_resource(BaseHandler, '/api/exists/EN/:id')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0") # served on the local network