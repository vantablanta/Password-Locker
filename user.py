class User:
    """
    class to define the user object and it methods 
    """
    users = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        User.users.append(self)

    def delete_user(self):
        User.users.remove(self)

    @classmethod
    def display_users(cls):
        return cls.users

    @classmethod
    def find_user__by_number(cls, number):
        for user in cls.users:
            if user.password == number:
                return user

    @classmethod
    def user_exists(cls, number):
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
        Credentials.accounts.append(self)

    def delete_account(self):
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
        for account in cls.accounts:
            if account.account_username == number:
                return True
