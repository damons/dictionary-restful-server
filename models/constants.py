""""This module is kind of used as a config file, may be replaced by a configuration file in the future"""
from bidict import bidict

DB_ADDRESS = "mongodb://localhost:27017/"
DB_NAME_TERMS = "db3"
DB_NAME_USERS = ""

TERMS_COLLECTION = "terms"
SCRIPTS_COLLECTION = "scripts"
RELATIONS_COLLECTION = "relationships"

USERS_COLLECTIONS = ""

PARSER_URL = "http://test-ieml.rhcloud.com/ScriptParser/rest/iemlparser"

# POST request
# data : iemltext
PARSE_SCRIPT = "iemlparser"

# POST request
GET_TREE = "/tree"

# POST request
GET_TABLES = "/tables"

GET_RELATIONSHIP = "/relationship2"


TAG_LANGUAGES = ["FR", "EN"]

RELATIONS = bidict({
    'ASCENDING': 'DESCENDING',
    'GERMAN': 'GERMAN'
})