import pytest
from pottery.converters.product_converter import product_entities_to_products,product_entity_to_product,product_to_product_entity
from pottery.entities.products import product_entity
from pottery.models.products import Product
import itertools

def test_product_entities_to_products():
    pe = product_entity()
    pe.id=1
    pe.name='mug'
    pe.title='mug'
    pe.description='mug'
    pe.price=10
    pe.weight='10'
    pe_list =[pe]
    p_list = product_entities_to_products(pe_list)
    assert isinstance(p_list[0],Product)
    for p,pe in itertools.product(p_list,pe_list):
        assert p.id == pe.id

def test_product_entity_to_product():
    pe = product_entity()
    pe.id = 1
    pe.name = 'mug'
    pe.title = 'mug'
    pe.description = 'mug'
    pe.price = 10
    pe.weight = '10'
    pe_to_p = product_entity_to_product(pe)
    assert isinstance(pe_to_p,Product)
    assert pe_to_p.id==pe.id

def test_product_to_product_entity():
    p = Product('mug','mug','mug','10','10',10,'mug',1)
    p_to_pe=product_to_product_entity(p)
    assert isinstance(p_to_pe,product_entity)
    assert p_to_pe.id==p.id


