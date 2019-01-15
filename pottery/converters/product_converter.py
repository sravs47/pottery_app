from pottery.entities.products import product_entity
from pottery.models.products import Product

def product_to_product_entity(product):
    #convert and return back a product entity
    # products.Product(id=produname=product_entity['name'],)
    p_to_pe = product_entity(id=product.id,name=product.name,title=product.title,description=product.description,weight=product.weight,dimentions=product.dimentions,price=product.price,image=product.image)
    return p_to_pe

def product_entity_to_product(product_entity):
    #convert and return back product
    # products.Product(id=produname=product_entity['name'],)
    pe_to_p =Product(name=product_entity.name,title=product_entity.title,description=product_entity.description,weight=product_entity.weight,dimentions=product_entity.dimentions,price=product_entity.price,image=product_entity.image,id=product_entity.id)
    return pe_to_p