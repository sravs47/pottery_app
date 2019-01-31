import functools
import flask
from pottery.resources.exceptions import PotteryException

def productvalidator(func):
    @functools.wraps(func)
    def wraps(*args,**kwargs):
        data = flask.request.get_json()
        errors =[]
        if len(data['name']) > 40:
            errors.append('Length of name is more than 40 characters')
        if data['price'] <= 0:
            errors.append('Price cannot be less than zero')
        if errors:
            raise PotteryException(errors)
        return func(*args, **kwargs)
    return wraps


def user_accountstvalidator(func):
    @functools.wraps(func)
    def wraps(*args , **kwargs):
        data = flask.request.get_json()
        errors =[]
        if len(data['phone_number'])>10:
            errors.append('Lenght of phone number is more than 10 numbers')
        if len(data['email'])>25:
            errors.append('Length of email address is greater than 25 characters')
        if errors:
            raise PotteryException(errors)
        return func(*args , **kwargs)
    return wraps













