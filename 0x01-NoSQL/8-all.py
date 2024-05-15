#!/usr/bin/env python3
'''List all '''
import pymongo


def list_all(mongo_collection):
    '''List all doc in collection'''
    docs = mongo_collection.find({})
    if docs.count() == 0:
        return []
