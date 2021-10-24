class credentials():
    """"

    credentials class to create new objects of credentials
    """
    credentials_list = []

    def __init__(self, account, userName, password):

        self.account = account
        self.userName = userName
        self.password = password

    def save_details(self):
        """
        function for saving user objects to credential-list
        """
        credentials.credentials_list.append(self)

    print(
        "Welcome to your new Password manager. To continue select '1' to login or '2' to create a new account:")
    print("\n1. Login \n2. Register new account")
    user_option = input()
