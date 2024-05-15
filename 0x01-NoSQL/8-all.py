#!/usr/bin/env python3
'''List all '''
import pymongo


def list_all(mongo_collection):
    mongo_collection.find()
