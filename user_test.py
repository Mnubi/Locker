import unittest # Importing the unittest module
from user import User # Importing the user class
class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    Args:
        unittest.TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.user1 = User( "mnubi", "12345") #create user object
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.user1.username,"mnubi")
        self.assertEqual(self.user1.password,"12345")
    def test_save(self):
        '''
        test_save test case to test if the user object is saved into
         the user_list
        '''
        self.user1.save_user()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()