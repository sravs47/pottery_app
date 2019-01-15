import json
from flask import Response
from pottery.models.products import Product
JSON_MIME_TYPE='application/json'


def search_prod(prods,product_id):
    for p in prods:
        if p['id']==product_id:
            print(p)
            return p


def to_dict(obj):
    return obj.__dict__
