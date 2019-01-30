import json
from flask import Response
from pottery.models.products import Product
JSON_MIME_TYPE='application/json'

def to_dict(obj):
    return obj.__dict__
