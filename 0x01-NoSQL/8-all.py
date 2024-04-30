#!/usr/bin/env python3

from pymongo import MongoClient

client = MongoClient()

def list_all():
  db = client['my_db']

  collection = db["school"]

  collectionlist = []

  for doc in collection.find():
      collectionlist.append(doc)

  return collectionlist
