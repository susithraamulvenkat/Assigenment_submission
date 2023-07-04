from pymongo import MongoClient
from scripts.constants import app_configurations
import logging

logger = logging.getLogger(__name__)


class Mongodb:
    def __init__(self):
        self.client = MongoClient(app_configurations.mongodb)
        self.db = self.client[app_configurations.db]

    def connect_collection(self, collection_name):
        return self.db[collection_name]

    def insert_one(self, collection, document):
        try:
            collection.insert_one(document)
            logger.info("Document inserted successfully")
            return True
        except Exception as e:
            logger.error(f"Error inserting document: {str(e)}")
            return False

    def find_one(self, collection, query):
        try:
            return collection.find_one(query)
        except Exception as e:
            logger.error(f"Error finding document: {str(e)}")
            return None

    def update_one(self, collection, filter_query, update_query):
        try:
            collection.update_one(filter_query, update_query)
            logger.info("Document updated successfully")
            return True
        except Exception as e:
            logger.error(f"Error updating document: {str(e)}")
            return False

    def delete_one(self, collection, query):
        try:
            collection.delete_one(query)
            logger.info("Document deleted successfully")
            return True
        except Exception as e:
            logger.error(f"Error deleting document: {str(e)}")
            return False