import random
import string

class User:
    """"""
    user_list = []

    def __init__(self, account, username, password ):
        self.username = username
        self.account = account
        self.password = password

    def save_user(self):
            User.user_list.append(self)

    def delete(self):
        User.user_list.remove(self)
  

