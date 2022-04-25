import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
    """"""
    new_user = User("Michelle", "pass")
    
    def setup(self):
        self.new_user = User("Michelle", "pass")

    def test_init(self):
        self.assertEqual(self.new_user.username, "Michelle")
        self.assertEqual(self.new_user.password, "pass")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users), 1)

    def test_delete_user(self):
        print(len(User.users))
        self.assertEqual(len(User.users), 0)


if __name__ == '__main__':
    unittest.main()

