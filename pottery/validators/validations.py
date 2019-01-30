import functools
import flask
from pottery.resources.exceptions import PotteryException

def productvalidator(func):
    @functools.wraps(func)
    def wraps(*args,**kwargs):
        data = flask.request.get_json()
        errors =[]
        print(data)
        if len(data['name']) > 40:
            errors.append('Length of name is more than 40 characters')
        if data['price'] > 200:
            errors.append('Length of name is more than 200 grams')
        if errors:
            raise PotteryException(errors)
        return func(*args, **kwargs)
    return wraps

















# if len(request.json['name']) > 40:
#     raise Exception("Length greater than 40")


