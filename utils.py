# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import yaml
from pymongo import MongoClient


def connect_to_mongo(func):
    """
    Decorator that enables connection to mongodb.
    """
    with open("config.yaml") as f:
        d = yaml.load(f)
    conn = MongoClient(d["host"], port=d["port"])
    db = conn[d["database"]]
    coll = db[d["collection"]]

    def connected_func(requests):
        func(requests, coll=coll)

    return connected_func


def dummy_response(response):
    """
    Dummy placeholder for httpresponse
    """
    print(response)
