#!/usr/bin/env python3
"""This Python script returns all students sorted by average score"""


def top_students(mongo_collection):
    """Mongo_collection will be the pymongo collection object,
    the top must be ordered. The return with key = averageScore"""
    collection_objects = {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {'$avg': '$topics.score'},
                'topics': 1,
                }
            }

    sort_objects = {'$sort': {'averageScore': -1}}
    results = mongo_collection.aggregate([collection_object, sort_objects])
    return results
