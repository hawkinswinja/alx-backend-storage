#!/usr/bin/env python3
"""
    11-schools_by_topic
    Author: @hawkinswinja
"""


def schools_by_topic(mongo_collection, topic):
    """filters school with topic in topics"""
    return mongo_collection.find({"topics": topic})
