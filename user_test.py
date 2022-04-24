import unittest

from requests import delete
from user import User

class TestUser(unittest.TestCase):
    """"""

    def setup(self):
        self.new_user = User("Facebook", "Michelle", "pass")

    def test_init(self):
        self.assertEqual(self.new_user.account, "Facebook")
        self.assertEqual(self.new_user.username, "Michelle")
        self.assertEqual(self.new_user.password, "pass")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
       """"""

if __name__ == '__main__':
    unittest.main()

