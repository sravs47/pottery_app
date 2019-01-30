# from pottery.resources.product_catalog import
from unittest.mock import patch,Mock
from pottery.models.products import Product as product_model
from pottery.resources.product_catalog import get_products
import pytest
import flask


# @patch('pottery.middleware.product_orchestrator.product_middleware.get_products')
# def test_get_products(mocker):
    # path = '~/collection'
    # p1 =product_model('mug','mug','mug','10','10',10,'mug',1)
    # with patch('pottery.middleware.product_orchestrator.product_middleware.get_products') as mock_get_products, \
    #         patch('pottery.resources.product_catalog.request.args.get') as mock_api:
    #     mock_api.return_value.limit=10
    #     mock_api.return_value.marker=0
    #     mock_get_products.return_value =[p1]
    #
    #     response = get_products()
    #
    #     print(response)



@patch('pottery.middleware.product_orchestrator.product_middleware.get_products')
@patch('flask.request')
def test_get_products(mocking,flask_mock):
    print(mocking)
    p1 = product_model('mug', 'mug', 'mug', '10', '10', 10, 'mug', 1)
    mocking.return_value = [p1]
    flask_mock.args = {'limit':1,'marker':2}
    response = get_products()
    assert response.status_code == 200
    assert isinstance(response,flask.Request)




