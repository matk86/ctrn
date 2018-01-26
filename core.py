# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

from utils import connect_to_mongo, dummy_response

"""
This module defines the functions for adding and searching compunds to the database.
From a django app perspective these functions constitute the contents of the views.py module.
"""


@connect_to_mongo
def add(request, coll=None):
    """
    Add compound to the database.

    Args:
        request:
        coll: pymongo collection instance

    Returns:
        a dummy response (in web app this should be replaced by a proper httpresponse)
    """
    if request.method == 'POST':
        compound = request.POST.get('compound')
        properties = request.POST.get('properties')
        for pi in properties:
            d = {"compound": compound.lower()}
            d[pi["propertyName"].lower()] = pi["propertyValue"].lower()
            coll.insert_one(d)
            return dummy_response("inserted")


@connect_to_mongo
def search(request, coll=None):
    """
    Add compound to the database.

    Args:
        request:
        coll: pymongo collection instance

    Returns:
        a dummy response (in web app this should be replaced by a proper httpresponse)
    """
    results = None
    if request.method == 'GET':
        compound = request.GET.get('compound')
        value = compound["value"].lower()
        query = {"compound": {"$regex": "\w*{}+".format(value)}}
        properties = request.GET.get('properties')
        for pi in properties:
            logic = pi["logic"]
            value = float(pi["value"]) if logic not in ["eq"] else pi["value"]
            query[pi["name"].lower()] = {"${}".format(): value}
        results = {"results": list(coll.find(query))}

    return dummy_response(results)
