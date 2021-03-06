import unittest
from credential import Credential
class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Setup for the test
        """
        self.new_credentials = Credential("Twitter","username", "12345")
    def test_init(self):
        """
            test to check credentials object is created
        """
        self.assertEqual(self.new_credentials.account_site, "Twitter")
        self.assertEqual(self.new_credentials.account_username, "username")
        self.assertEqual(self.new_credentials.account_password, "12345")

    def test_save_credentials(self):
        '''
        check if the credentials object is saved to account_user []
        '''
        self.assertEqual(len(Credential.user_credentials), 0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credential.user_credentials), 1)

    def test_delete_credentials(self):
        """
        check if saved credential from the users credentials is deleted
        """
        self.assertEqual(len(Credential.user_credentials),0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credential.user_credentials),1)
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credential.user_credentials),0)

    def test_find_credentials_by_site(self):
        '''
        test to check if we can find a credential by site
        '''
        self.found_credentials = Credential.find_by_account_site("Twitter")

if __name__ == '__main__':
    unittest.main()