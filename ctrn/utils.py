# coding: utf-8

import os
import yaml
from pymongo import MongoClient

module_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))


def connect_to_mongo(func):
    """
    Decorator that enables connection to mongodb.
    """
    with open(os.path.join(module_dir, "config.yaml")) as f:
        d = yaml.load(f)
    conn = MongoClient(d["host"], port=d["port"])
    db = conn[d["database"]]
    coll = db[d["collection"]]

    def connected_func(requests):
        return func(requests, coll=coll)

    return connected_func


class DummyResponse(object):
    """
    Dummy placeholder for httpresponse
    """
    def __init__(self, response):
        self.response = response
