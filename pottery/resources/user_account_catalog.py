from flask import Blueprint,request,Response
from .utils import JSON_MIME_TYPE, to_dict
from pottery.middleware.accounts_orchestrator import accounts_middleware
import json
from pottery.validators.validations import user_accountstvalidator
from pottery.models import accounts
from pottery.resources.exceptions import PotteryException


useraccountapp = Blueprint('useraccount',__name__)

@useraccountapp.route('/account/<int:account_id>')
def get_account(account_id):
    user = accounts_middleware().get_account(account_id)
    resp = to_dict(user)
    return Response(json.dumps(resp),200,mimetype=JSON_MIME_TYPE)

@useraccountapp.route('/accounts',methods =['POST'])
@user_accountstvalidator
def add_user():
    status = 201
    resp = None
    body = request.json
    user =accounts.Account(body['first_name'],body['last_name'],body['user_name'],body['phone_number'],body['address1'],body['address2'],body['email'],body['id'])
    try:
        acc = accounts_middleware().create_account(user)
        result = to_dict(acc)
        resp = json.dumps(result)
    except PotteryException as e:
        if 'A5' in str(e):
            status = 400
            resp = str(e)
    except Exception as e:
        status = 500
        print(str(e))
        resp = str(e)
    return Response(resp,status=status,mimetype=JSON_MIME_TYPE)

@useraccountapp.route('/account/<int:account_id>',methods=['DELETE'])
def del_user(account_id):
    status = 204
    try:
        accounts_middleware().del_account(account_id)
    except PotteryException as e:
        if 'A6' in str(e):
            status = 400
    return Response(status=status)

@useraccountapp.route('/account/<int:account_id>',methods = ['PUT'])
def update_user(account_id):
    body = request.json
    status = 201
    resp = None
    user = accounts.Account(body['first_name'], body['last_name'], body['user_name'], body['phone_number'],
                            body['address1'], body['address2'], body['email'], body['id'])
    try:
        acc = accounts_middleware().update_account(account_id,user)
        result = to_dict(acc)
        resp = json.dumps(result)
    except PotteryException as e:
        if 'A7' in str(e):
            status = 400
    return Response(resp, status=status,mimetype=JSON_MIME_TYPE)

