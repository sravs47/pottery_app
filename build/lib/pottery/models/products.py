

class Product(object):
    def __init__(self,name,title,description,weight,dimentions,price,image,id=None):
        self.id=id
        self.name=name
        self.title= title
        self.description=description
        self.weight=weight
        self.dimentions=dimentions
        self.price = price
        self.image = image
