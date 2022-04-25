class User:
    """
    class to define the user object and it methods 
    """
    users = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        """
        Function to save a user
        """
        User.users.append(self)

    def delete_user(self):
        """
        Function to delete a user 
        """
        User.users.remove(self)

    @classmethod
    def display_users(cls):
        """
        Function to save a user
        """
        return cls.users

    @classmethod
    def find_user__by_number(cls, number):
        """
        Function to find a user by username
        """
        for user in cls.users:
            if user.password == number:
                return user

    @classmethod
    def user_exists(cls, number):
        """
        Function to check if a user exists
        """
        for user in cls.users:
            if user.username == number:
                return True


class Credentials:
    """
    class to define the credentials object and its methods
    """
    accounts = []

    def __init__(self, account_username, account_name, account_password):
        self.account_username = account_username
        self.account_name = account_name
        self.account_password = account_password

    def save_account(self):
        """
        Function to save an account
        """
        Credentials.accounts.append(self)

    def delete_account(self):
        """
        Function to delete and account
        """
        Credentials.accounts.remove(self)

    @classmethod
    def display_account(cls):
        """
        Method that displays all the accounts 
        """
        return cls.accounts

    @classmethod
    def find_account_by_number(cls, number):
        """
        Method that takes in a account_username and returns a credential that matches that account
        """
        for account in cls.accounts:
            if account.account_username == number:
                return account

    @classmethod
    def user_exists(cls, number):
        """
        Method to check if a  user exists
        """
        for account in cls.accounts:
            if account.account_username == number:
                return True
