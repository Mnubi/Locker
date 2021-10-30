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
    
    def test_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.user1.save_user()
        another_user = User("Kelsey", "1234")
        another_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        self.user1.save_user()
        another_user = User("Kelsey", "1234")
        another_user.save_user()
        self.user1.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_by_username(self):
        self.user1.save_user()
        another_user = User("Kelsey", "1234")
        another_user.save_user()
        found_user = User.find_by_username("username")

    def test_user_exists(self):
        self.user1.save_user()
        another_user = User( "Kelsey" ,"1234")
        another_user.save_user()
        user_exists = User.user_exists("Kelsey")
        self.assertTrue(user_exists)

if __name__ == '__main__':
    unittest.main()