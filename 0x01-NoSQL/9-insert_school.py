#!/usr/bin/env python3
"""This module contains a single function insert school"""


def insert_school(mongo_collection, **kwargs):
    """add new document kwargs to mongo_collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
