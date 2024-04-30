#!/usr/bin/env python3
"""
update a topic in document
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    mongo_collection.update_many(
      {'name': name},
      {'$set': {'topics': topics}}
    )
