import random
import string
class Credential():
    user_credentials = []
    def __init__(self, account_site, account_username, account_password):
        self.account_site = account_site
        self.account_username =  account_username
        self.account_password =  account_password

    def save_credentials(self):
        '''
        save credentials into user_credentials
        '''
        Credential.user_credentials.append(self)