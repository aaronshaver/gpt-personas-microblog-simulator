import unittest
import users.users

class Case(unittest.TestCase):

    def setUp(self):
        self.users = users.users.Users('test_users')

    def test_get_user_content_basic(self):
        result = self.users.get_user_prompt()
        self.assertIn('"user_name": "Bill"', result)
        self.assertIn('Bill is a prety cool dude', result)

    def test_get_user_content_has_all_fields(self):
        result = self.users.get_user_prompt()
        self.assertIn('"user_name"', result)
        self.assertIn('"user_background"', result)
        self.assertIn('"recent_messages"', result)