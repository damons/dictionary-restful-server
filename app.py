from flask import Flask
from flask_restful import Api

from handlers import *

app = Flask(__name__)
api = Api(app)


### This is the api's routing table ###

# Get all the IEML terms
api.add_resource(GetAllIEMLTermsHandler, '/api/allieml');

# Get an accesss token to the client
api.add_resource(AuthenticationHandler, '/client/authenticate')

### Relations editing and listing endpoints
api.add_resource(GetRelationVisibilityHandler, '/api/getRelVisibility')
api.add_resource(AddRelationVisibilityHandler, '/api/addRelVisibility') # requires login
api.add_resource(RemoveRelationVisibility, '/api/remRelVisibility') # requires login
api.add_resource(ToggleRelationVisibilityHandler, '/api/toggleRelVisibility')
api.add_resource(GetRelationsHandler, '/api/rels')

### IEML edition endpoints
api.add_resource(NewIEMLTermHandler, '/api/newieml') # requires login
api.add_resource(UpdateIEMLTermHandler, '/api/updateieml') # requires login
api.add_resource(RemoveIEMLTermHandler, '/api/remieml/<term_id>') # requires login

### search handlers
api.add_resource(SearchIEMLHandler, '/api/exists/ieml/<term_id>')
api.add_resource(SearchFRHandler, '/api/exists/FR/<term_id>')
api.add_resource(SearchENHandler, '/api/exists/EN/<term_id>')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080) # served on the local network