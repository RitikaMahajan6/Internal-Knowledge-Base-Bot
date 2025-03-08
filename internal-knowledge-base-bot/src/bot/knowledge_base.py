class KnowledgeBase:
    def __init__(self, mongo_client):
        self.mongo_client = mongo_client
        self.db = self.mongo_client['knowledge_base']
        self.collection = self.db['documents']

    def query(self, query_text):
        results = self.collection.find({"$text": {"$search": query_text}})
        return [result for result in results]

    def update(self, document_id, update_data):
        self.collection.update_one({"_id": document_id}, {"$set": update_data})

    def add_document(self, document):
        self.collection.insert_one(document)

    def delete_document(self, document_id):
        self.collection.delete_one({"_id": document_id})