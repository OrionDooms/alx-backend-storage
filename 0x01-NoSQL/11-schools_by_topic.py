#!/usr/bin/env python3
"""The script returns a list of school with a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """The list is stored in a mongo database"""
    temp = mongo_collection.find({"topics": topic})
    results = list(temp)
    return results
