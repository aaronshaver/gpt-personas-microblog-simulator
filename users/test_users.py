import unittest
import users.users
import io_helper.io_helper as io_helper

class Case(unittest.TestCase):

    def setUp(self):
        self.users = users.users.Users('test_users')
        io_helper.create_messages_table()

    def test_get_user_content_has_user_name_user_background(self):
        result = self.users.get_user_prompt()
        self.assertTrue('"current_user":"Bill"' in result or '"current_user":"Jill"' in result)
        self.assertTrue('Bill is a prety cool dude' in result or 'Jill is a tall person' in result)

    def test_get_user_content_has_all_fields(self):
        result = self.users.get_user_prompt()
        self.assertIn('"current_user"', result)
        self.assertIn('"user_background"', result)
        self.assertIn('"recent_message"', result)