from pottery.entities.user_accounts import user_accounts
from pottery.models.accounts import Account

def account_to_account_entity(user):
    a_to_ae = user_accounts(id = user.id , first_name = user.first_name, last_name = user.last_name,user_name=user.user_name,phone_number=user.phone_number,address1=user.address1,address2=user.address2,email=user.email)
    return a_to_ae

def account_entity_to_account(account_entity):
    ae_to_a = Account(first_name=account_entity.first_name,last_name=account_entity.last_name,user_name=account_entity.user_name,phone_number=account_entity.phone_number,address1=account_entity.address1,address2=account_entity.address2,email=account_entity.email,id=account_entity.id)
    return ae_to_a

def account_entities_to_accounts(account_entities):
    aes_to_a=[]
    if account_entities!=None:
        for aes in account_entities:
            aes_to_a.append(account_entity_to_account(aes))
    return aes_to_a
