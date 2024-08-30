#!/usr/bin/env python3
"""This Python script returns all students sorted by average score"""


def top_students(mongo_collection):
    """Mongo_collection will be the pymongo collection object,
    the top must be ordered. The return with key = averageScore"""
    pipeline = [
            {
                '$project': {
                    'name': 1,
                    'scores': 1,
                    'averageScore': {'$avg': '$scores'},
                    }
                },
            {
                '$sort': {'averageScore': -1}
                }
            ]

    temp = mongo_collection.aggregate(pipeline)
    result = list(temp)
    return result
