import unittest
import users.users

class Case(unittest.TestCase):

    def setUp(self):
        self.users = users.users.Users('./test_characters')

    def test_get_user_content_basic(self):
        result = self.users.get_user_prompt()
        self.assertIn('"user_name": "Bill"', result)