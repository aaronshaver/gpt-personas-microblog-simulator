import unittest
import users.users

class Case(unittest.TestCase):

    def setUp(self):
        self.users = users.users.Users('test_users')

    def test_get_user_content_has_user_name_user_background(self):
        result = self.users.get_user_prompt()
        self.assertTrue('"user_name": "Bill"' in result or '"user_name": "Jill"' in result)
        self.assertTrue('Bill is a prety cool dude' in result or 'Jill is a tall person' in result)

    def test_get_user_content_has_all_fields(self):
        result = self.users.get_user_prompt()
        self.assertIn('"user_name"', result)
        self.assertIn('"user_background"', result)
        self.assertIn('"recent_messages"', result)