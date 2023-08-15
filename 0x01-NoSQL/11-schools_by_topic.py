#!/usr/bin/env python3
"""
Script tthat returns list of school offering
a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """List schools offering given topic"""
    results = mongo_collection.find({"topics": topic})
    return results
