from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoUtils:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def create_document(self, collection_name, document):
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        return str(result.inserted_id)

    def read_document(self, collection_name, document_id):
        collection = self.db[collection_name]
        document = collection.find_one({"_id": ObjectId(document_id)})
        return document

    def update_document(self, collection_name, document_id, updated_data):
        collection = self.db[collection_name]
        result = collection.update_one({"_id": ObjectId(document_id)}, {"$set": updated_data})
        return result.modified_count

    def delete_document(self, collection_name, document_id):
        collection = self.db[collection_name]
        result = collection.delete_one({"_id": ObjectId(document_id)})
        return result.deleted_count

    def list_documents(self, collection_name):
        collection = self.db[collection_name]
        return list(collection.find())