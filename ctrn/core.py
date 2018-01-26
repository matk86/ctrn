# coding: utf-8

from .utils import connect_to_mongo, DummyResponse

"""
This module defines the functions for adding and searching compounds to the database.
From a web app perspective these functions(the decorated ones at the bottom) constitute the 'views'.
"""


def add_(request, coll=None):
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
        d = {"compound": compound}
        for pi in properties:
            d[pi["propertyName"].lower()] = pi["propertyValue"].lower()
        coll.insert_one(d)
        return DummyResponse(request)


def search_(request, coll=None):
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
        value = compound["value"]
        query = {"compound": {"$regex": "\w*{}+".format(value)}}
        properties = request.GET.get('properties')
        for pi in properties:
            logic = pi["logic"]
            value = pi["value"].lower() #float(pi["value"]) if logic not in ["eq"] else
            query[pi["name"].lower()] = {"${}".format(logic): value}

        results = {"results": []}
        for d in coll.find(query, {"_id": 0}):
            dt = {"compound": d.pop("compound"), "properties": []}
            for k, v in d.items():
                dt["properties"].append({"propertyName": k, "propertyValue": v})
            results["results"].append(dt)

    return DummyResponse(results)


add = connect_to_mongo(add_)
search = connect_to_mongo(search_)
