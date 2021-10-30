class User:
    """
    Class that generates new users
    """
    user_list = [] # Empty user list
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_uer method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)