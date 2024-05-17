#!/usr/bin/env python3
'''List all '''
import pymongo


def list_all(mongo_collection):
    '''List all doc in collection'''
    docs = mongo_collection.count_documents({})
    if docs == 0:
        return []
    return mongo_collection.find({})

