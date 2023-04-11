#!/usr/bin/env python3
"""
    10-update_topics
    Author: @hawkinswinja
"""


def update_topics(mongo_collection, name, topics):
    """
        Updates document with name=name and adds topics
        @name: value for name to filter
        @topics: list of topics to add
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
