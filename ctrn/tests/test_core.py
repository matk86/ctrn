# coding: utf-8

import unittest
from pymongo import MongoClient

from ctrn.core import add_, search_


class DummyRequest(object):
    def __init__(self, d):
        self.POST = d
        self.GET = d


class TestCore(unittest.TestCase):

    def test_add(self):
        conn = MongoClient("localhost", port=27017)
        db = conn["test_db"]
        coll = db["test_coll"]
        coll.delete_many({})
        d = {
            "compound": "GaN",
            "properties": [
                {
                    "propertyName": "Band gap",
                    "propertyValue": "3.4"
                },
                {
                    "propertyName": "color",
                    "propertyValue": "white"
                }
            ]
        }
        request = DummyRequest(d)
        request.method = "POST"
        response = add_(request, coll)
        self.assertDictEqual(response.response.POST, {
            'compound': 'GaN',
            'properties': [
                {'propertyName': 'Band gap', 'propertyValue': '3.4'},
                {'propertyName': 'color', 'propertyValue': 'white'}]})

    def test_search(self):
        conn = MongoClient("localhost", port=27017)
        db = conn["test_db"]
        coll = db["test_coll"]
        d = {
              "compound": {
                "logic": "contains",
                "value": "Ga"
              },
              "properties": [
                {
                  "name": "Band gap",
                  "value": "3.3",
                  "logic": "gt"
                },
                {
                  "name": "color",
                  "value": "white",
                  "logic": "eq"
                }
              ]
            }
        request = DummyRequest(d)
        request.method = "GET"
        response = search_(request, coll)
        self.assertDictEqual(response.response, {
            'results': [
                {'compound': 'GaN',
                 'properties': [
                     {'propertyName': 'band gap',
                      'propertyValue': '3.4'},
                     {'propertyName': 'color',
                      'propertyValue': 'white'}
                 ]
                 }
            ]
        })


if __name__ == "__main__":
    unittest.main()
