class Account(object):
    def __init__(self,first_name,last_name,user_name,phone_number,address1,address2,email,id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.phone_number = phone_number
        self.address1 = address1
        self.address2 = address2
        self.email = email