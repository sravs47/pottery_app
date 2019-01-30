from pottery.entities import products
from pottery.resources.exceptions import PotteryException
from pottery.converters import product_converter
from pottery.resources.utils import to_dict
import pymongo


# convert the product object which comes from product_catalog to product entity object(database object) and save.
class product_middleware:
    def create_product(self, product):
        try:
            if products.product_entity.objects.get({'_id': product.id}) != None:
                raise PotteryException(f'A1: Pottery item with the id {product.id} already exist')
        except Exception as e:
            if e.__class__.__name__ == 'PotterException':
                raise e
            elif e.__class__.__name__ =='DoesNotExist':
                pass
            else:
                raise Exception("Internal server error")

        prod_data = products.product_entity(id=product.id, name=product.name, title=product.title,
                                            description=product.description, weight=product.weight,
                                            dimentions=product.dimentions, price=product.price,
                                            image=product.image).save()
        return self.get_product(product.id)

    def get_product(self, product_id):
        prod_data = products.product_entity.objects.get({'_id': product_id})
        return product_converter.product_entity_to_product(prod_data)

    def get_products(self,limit=10,marker=0):
        print(limit)
        print(marker)
        product_entities = products.product_entity.objects.order_by([('_id',pymongo.ASCENDING)]).skip(limit*marker).limit(limit)
        return product_converter.product_entities_to_products(product_entities)

    def delete_product(self, product_id):
        if products.product_entity.objects.get({'_id':product_id}) == None :
            raise PotteryException(f'A2: Pottery item with the id {product_id} Doesnt exist')
        prod_data = products.product_entity.objects.get({'_id': product_id}).delete()

    def update_product(self,product_id,product):
        gp = self.get_product(product_id)
        resp = to_dict(gp)
        if resp['id']!=product.id:
            raise PotteryException('Id missmatch')

        try:
           product_entity = products.product_entity.objects.get({'_id':product_id})
           product_entity.name = product.name
           product_entity.weight = product.weight
           product_entity.title=product.title
           product_entity.description=product.description
           product_entity.dimentions=product.dimentions
           product_entity.price=product.price
           product_entity.image=product.image
           product_entity.save()
           return self.get_product(product_id)
        except:
            raise PotteryException(f'A3: pottery ite with the id {product_id} Does not exist')










