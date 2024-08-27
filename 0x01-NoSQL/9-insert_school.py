#!/usr/bin/env python3
"""This script inserts a new document in the collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """The object is inserted in a collection on a mongo database"""
    temp = mongo_collection.insert_one(kwargs)
    return temp.inserted_id
