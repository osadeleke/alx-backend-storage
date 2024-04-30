#!/usr/bin/env python3
"""
insert a document in a collection
"""
from pymongo import  MongoClient

def insert_school(mongo_collection, **kwargs):
  """
  insert a document in a collection using
  insert_one()
  """
  new_document = mongo_collection.insert_one(kwargs)

  return new_document.inserted_id