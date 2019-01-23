
from pymodm import fields, MongoModel
#product catalog model class for Database.
class product_entity(MongoModel):
    id = fields.IntegerField(primary_key=True)
    name = fields.CharField()
    title = fields.CharField()
    description = fields.CharField()
    weight = fields.CharField()
    dimentions = fields.CharField()
    price = fields.IntegerField()
    image = fields.CharField()


