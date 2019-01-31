from pottery.entities import user_accounts
from pottery.resources.exceptions import PotteryException
from pottery.resources.utils import to_dict
from pottery.converters import accounts_converter
import pymongo

class accounts_middleware:
    def create_account(self,account):
        try:
            if user_accounts.user_accounts.objects.get({'_id':account.id})!=None:
                raise PotteryException(f'A5 : Account with the id {account.id} already exists')
        except Exception as e:
            if e.__class__.__name__ == 'PotteryException':
                raise e
            elif e.__class__.__name__=='DoesNotExist':
                pass
            else:
                raise Exception("Internal server error: "+str(e))

        account_data = user_accounts.user_accounts(id = account.id,first_name=account.first_name,last_name=account.last_name,user_name=account.user_name,phone_number = account.phone_number , address1 = account.address1, address2 =account.address2 , email = account.email).save()
        return self.get_account(account.id)

    def get_account(self,account_id):
        acc_data = user_accounts.user_accounts.objects.get({'_id':account_id})
        return accounts_converter.account_entity_to_account(acc_data)

    def del_account(self,account_id):
        if user_accounts.user_accounts.objects.get({'_id':account_id}) == None:
            raise PotteryException(f'A6: User with the id {account_id} doest exist')
        acc_data = user_accounts.user_accounts.objects.get({'_id':account_id}).delete()

    def update_account(self,account_id,account):
        acc = self.get_account(account_id)
        resp = to_dict(acc)
        if resp['id'] !=account.id:
            raise PotteryException('ID mismatch')
        try:
            ua = user_accounts.user_accounts.objects.get({'_id':account_id})
            ua.first_name =account.first_name
            ua.last_name = account.last_name
            ua.user_name = account.user_name
            ua.phone_number = account.phone_number
            ua.address1 = account.address1
            ua.address2 = account.address2
            ua.email = account.email
            ua.save()
            return self.get_account(account_id)
        except:
            raise PotteryException(f'A7: Account with the id {account_id} Does not exist')

