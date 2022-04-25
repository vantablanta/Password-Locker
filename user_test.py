import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
    """"""
    new_user = User("Michelle", "pass")
    new_credentials = Credentials("njeri", "facebook", "1234")

    def setup(self):
        self.new_user = User("Michelle", "pass")
        self.new_credentials = Credentials("njeri", "facebook", "1234")

    def test_init(self):
        self.assertEqual(self.new_user.username, "Michelle")
        self.assertEqual(self.new_user.password, "pass")
        self.assertEqual(self.new_credentials.account_username, "njeri")
        self.assertEqual(self.new_credentials.account_name, "facebook")
        self.assertEqual(self.new_credentials.account_password, "1234")

    def test_save(self):
        self.new_user.save_user()
        self.new_credentials.save_account()
        self.assertEqual(len(User.users), 1)
        self.assertEqual(len(Credentials.accounts), 1)

    def test_delete(self):
        self.assertEqual(len(User.users), 0)
        self.assertEqual(len(Credentials.accounts), 0)


if __name__ == '__main__':
    unittest.main()

