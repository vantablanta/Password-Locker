from credentials import Credentials
class User(Credentials):
    """
    class that defines the User object
    """
    

    def __init__(self, username, account, password):
        self.username = username
        self.account = account
        self.password  = password

        users = {
        'account':self.account,
        'username': self.username,
        'password':self.password
        }


        print(users)

user1 = User("Michelle", "Twitter", Credentials.password1)
    