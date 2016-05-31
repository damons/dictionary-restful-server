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

### Annotation editing endpoints
api.add_resource(GetAnnotationsHandler, '/api/getannotations')
api.add_resource(RemoveAnnotationsHandler, '/api/removeannotation')
api.add_resource(AddAnnotationHandler, '/api/addannotation')

### Relations editing and listing endpoints
api.add_resource(GetRelationVisibilityHandler, '/api/getRelVisibility')
api.add_resource(AddRelationVisibilityHandler, '/api/addRelVisibility') # requires login
api.add_resource(RemoveRelationVisibility, '/api/remRelVisibility') # requires login
api.add_resource(ToggleRelationVisibilityHandler, '/api/toggleRelVisibility')
api.add_resource(GetRelationsHandler, '/api/rels')

### IEML edition endpoints
api.add_resource(NewIEMLTermHandler, '/api/newieml') # requires login
api.add_resource(UpdateIEMLTermHandler, '/api/updateieml') # requires login
api.add_resource(RemoveIEMLTermHandler, '/api/remieml/:id') # requires login

### search handlers
api.add_resource(SearchIEMLHandler, '/api/exists/ieml/:id')
api.add_resource(SearchFRHandler, '/api/exists/FR/:id')
api.add_resource(SearchENHandler, '/api/exists/EN/:id')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0") # served on the local network