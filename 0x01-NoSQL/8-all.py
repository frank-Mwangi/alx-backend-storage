"""
List all documents in a collection
"""


def list_all(mongo_collection):
    """Function to list all documents"""
    documents = list(mongo_collection.find())
    return documents
