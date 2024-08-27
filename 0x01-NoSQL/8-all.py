#!/usr/bin/env python3
"""This python script List all documents"""


def list_all(mongo_collection):
    """The list is stored in a momgo database"""
    temp = mongo_collection.find()
    results = list(temp)
    return results
