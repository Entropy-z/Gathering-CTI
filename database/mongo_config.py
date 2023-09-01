from pymongo import MongoClient

class MongoDBHelper:
    def __init__(self, db_url, db_name, collection_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_document(self, document):
        result = self.collection.insert_one(document)
        return result.inserted_id

    def find_document(self, query):
        return self.collection.find_one(query)

    def list_documents(self, query=None):
        if query is None:
            cursor = self.collection.find()
        else:
            cursor = self.collection.find(query)

        documents = [document for document in cursor]
        return documents

    def close_connection(self):
        self.client.close()