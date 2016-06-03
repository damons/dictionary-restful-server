from pymongo import MongoClient

from helpers.metaclasses import Singleton
from models.constants import TERMS_COLLECTION, TAG_LANGUAGES, DB_NAME_TERMS, SCRIPTS_COLLECTION
from .constants import DB_ADDRESS, DB_NAME_TERMS


class DBConnector(object, metaclass=Singleton):
    """Automatically connects when instantiated"""

    def __init__(self):
        self.client = MongoClient(DB_ADDRESS)  # connecting to the db

        self.db_term = self.client[DB_NAME_TERMS]

        self.scripts = self.db_term[SCRIPTS_COLLECTION]
        self.terms = self.db_term[TERMS_COLLECTION]

class UsersQueries(DBConnector):
    """Simple connector for user logins and token check"""

    def __init__(self):
        super().__init__()
        pass
