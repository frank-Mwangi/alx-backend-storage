#!/usr/bin/env python3
"""
Change all topics of a school document
based on the name
"""


def update_topics(mongo_collection, name, topics):
    """update school topics based on the name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}})
