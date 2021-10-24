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

    print(" " * 5)
    print("Welcome to your new Password manager. To continue select '1' to login or '2' to create a new account:")
    print("\n1. Login \n2. Register new account")
    print(" " * 5)
    user_option = input()

    if user_option == "1":
        print("Enter your account details")
        print('\n')
        account_name = input('Account: ')
        print('\n')
        user_name = input('User name: ')
        # print('\n')

        while True:
            print("\n1. To type your own pasword:\n2. To generate random Password")
            password_Choice = input().lower()
            if password_Choice == '1':
                password = input("Enter Password")

                break
            elif password_Choice == '2':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")

    else:

        print("      CREATE A NEW ACCOUNT!")
        print(" ")

        print("what is your username?..")
        username = input()
        print(" " * 3)

        print("what is your email address?..")
        email = input()
        print(" " * 3)

        print("create new password")
        password = input()
        print(" " * 3)

        print("confirm new password")
        cpassword = input()
        print(" " * 3)

        while password != cpassword:
            print("password did not match")
            print("enter your new password")
            password = input()
            print("confirm your new password")
            cpassword = input()
            
        else:
            print("Your password manager account for " +
                username + " has been created successfully")
            print('\n')
            print(" " * 3)
            print("proceed to login")
            print(" " * 3)
            print ("Enter username")
            login_username = input()
            print("enter password")
            login_password = input()
            print(" " * 3)

        while login_username != username or login_password != password:
            print("password did not match")
            print("enter your new password")
            password = input()

            print(" " * 3)
            print("confirm your new password")
            cpassword = input()
            print(" " * 3)
        
        else: 
            print("welcome back " + login_username)
            print('\n')
            