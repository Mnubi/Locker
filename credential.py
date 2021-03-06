import random
import string
class Credential():
    user_credentials= []
    def __init__(self, account_site, account_username, account_password):
        self.account_site = account_site
        self.account_username =  account_username
        self.account_password =  account_password

    def save_credentials(self):
        '''
        save credentials into user_credentials
        '''
        Credential.user_credentials.append(self)

    def delete_credentials(self):
        '''
        delete save credentials
        '''
        Credential.user_credentials.remove(self)
    @classmethod
    def find_by_account_site(cls, account_site):
        '''
        method that takes in a account_site and returns credentials
        '''
        for credential in cls.user_credentials:
            if credential.account_site == account_site:
                return credential
        return False
    @classmethod
    def display_credentials(cls):
        '''
        return credentials list
        '''
        return cls.user_credentials
    @classmethod
    def generate_password(cls, password_length):
        '''
           Method to generate random password for a user creating a new account in the the user_credentials.
        '''
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*<?>"
        return ''.join(random.choice(password) for i in range(password_length))





