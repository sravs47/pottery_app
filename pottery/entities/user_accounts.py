from pymodm import fields, MongoModel

class user_accounts(MongoModel):
    id = fields.IntegerField(primary_key=True)
    first_name = fields.CharField()
    last_name = fields.CharField()
    user_name = fields.CharField()
    phone_number = fields.CharField()
    address1 = fields.CharField()
    address2 = fields.CharField()
    email = fields.CharField()



