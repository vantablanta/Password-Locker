import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
    """"""

    def setup(self):
        self.new_user = User("Michelle", "pass")
        self.new_account = Credentials("Michelle","Facebook","pass")

    def test_init(self):
        self.assertEqual(self.new_user.username, "Michelle")
        self.assertEqual(self.new_user.password, "pass")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()

