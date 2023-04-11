#!/usr/bin/env python3
"""Display  all documents in the collection"""


def list_all(mongo_collection):
    """Lists all documents in the mongo_collection"""
    return mongo_collection.find()
