#!/usr/bin/env python3
"""This script changes all topics of a school document based on the name:"""


def update_topics(mongo_collection, name, topics):
    """The document(object) in the collection will update
    the name in the list"""
    temp_name = {"name": name}
    temp_update = {"$set": {"topics": topics}}
    result = mongo_collection.update_one(temp_name, temp_update)
