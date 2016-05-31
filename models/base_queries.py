from pymongo import MongoClient

from helpers.metaclasses import Singleton
from models.constants import TERMS_COLLECTION, TAG_LANGUAGES, DB_NAME_TERMS
from .constants import DB_ADDRESS, DB_NAME


class DBConnector(object, metaclass=Singleton):
    """Automatically connects when instantiated"""

    def __init__(self):
        self.client = MongoClient(DB_ADDRESS)  # connecting to the db

        self.db = self.client[DB_NAME] # opening a DB
        self.db_term = self.client[DB_NAME_TERMS]

        self.terms = self.db_term[TERMS_COLLECTION]
