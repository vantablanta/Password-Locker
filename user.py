class UserClass:
    """
    Create User class that generates new instances of a user.
    """
    user_list = []

    def __init__(self, account, username, password):
        """
        method that defines the properties of a user.
        """
        self.account = account
        self.username = username
        self.password = password

    def save_user(self):
        """
        A method that saves a new user instace into the user list
        """
        UserClass.user_list.append(self)
    

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        UserClass.user_list.remove(self)
