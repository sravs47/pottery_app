from flask import Response, request
import json
from pottery import app
from pottery.models import products, pagination
from .utils import JSON_MIME_TYPE, to_dict
from .Data import products_list
from pottery.middleware.product_orchestrator import product_middleware
from pottery.resources.exceptions import PotteryException
from logging import getLogger as logger


# get all products using pagination
@app.route('/products')
def get_products():
    limit = int(request.args.get('limit', 10))  # 10 is default value if limit is not sent
    marker = int(request.args.get('marker', 0))

    get_products = product_middleware().get_products(limit, marker)
    products = []
    for product in get_products:
        products.append(to_dict(product))

    paginated: dict = to_dict(pagination.Pagination(limit, marker, 'products'))

    resp = {
        'products':products,
        'pagination':paginated

    }
    return Response(json.dumps(resp), 200, mimetype=JSON_MIME_TYPE)


@app.route('/products/<int:product_id>')
def get_product(product_id):
    gp = product_middleware().get_product(product_id)
    resp = to_dict(gp)
    logger.info(resp)
    return Response(json.dumps(resp), 200, mimetype=JSON_MIME_TYPE)


@app.route('/products', methods=['POST'])
def add_product():
    status = 201
    resp = None
    body = request.json
    product = products.Product(body['name'], body['title'], body['description'], body['weight'], body['dimentions'],
                               body['price'], body['image'], body['id'])
    try:
        pm = product_middleware().create_product(product)
        result = to_dict(pm)
        resp = json.dumps(result)
    except PotteryException as e:
        if 'A1' in str(e):
            status = 400
            resp = str(e)
    except Exception as e:
        status = 500
        resp = str(e)
    return Response(resp, status=status, mimetype=JSON_MIME_TYPE)


@app.route('/products/<int:product_id>', methods=['DELETE'])
def del_product(product_id):
    status = 204
    try:
        product_middleware().delete_product(product_id)
    except PotteryException as e:
        if 'A2' in str(e):
            status = 400
    return Response(status=status)


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    body = request.json
    status = 201
    resp = None
    product = products.Product(body['name'], body['title'], body['description'], body['weight'], body['dimentions'],
                               body['price'], body['image'], body['id'])
    try:
        gp = product_middleware().update_product(product_id, product)
        result = to_dict(gp)
        resp = json.dumps(result)
    except PotteryException as e:
        if 'A3' in str(e):
            status = 400
    return Response(resp, status=status, mimetype=JSON_MIME_TYPE)
