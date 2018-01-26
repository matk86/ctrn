# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import csv
from utils import connect_to_mongo


@connect_to_mongo
def insert_to_mongo(filename, coll=None):
    """
    insert the given csv file to mongodb.

    Args:
        filename (str): path to the csv data file
        coll (pymongo.Collection): pymongo collection instance
    """
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            d = {"compound": row[0].lower(),
                 row[1].lower(): float(row[2]),
                 row[3].lower(): row[4].lower()}
            coll.insert_one(d)
