import unittest
import users.users
import io_helper.io_helper as io_helper
from shared import global_config

class Case(unittest.TestCase):

    def setUp(self):
        self.users = users.users.Users('test_users')
        io_helper.create_messages_table()

    def tearDown(self):
        pass

    def test_get_user_content_has_user_name_user_background(self):
        result = self.users.get_user_prompt()
        self.assertIn('current_user', result)
        self.assertTrue(result['current_user'] in ['Bill', 'Jill'])
        self.assertIn('current_user_background', result)
        self.assertTrue(result['current_user_background'] in ['Bill is a pretty cool dude', 'Jill is a tall person'])

    def test_get_user_content_has_all_fields(self):
        result = self.users.get_user_prompt()
        self.assertIn('current_user', result)
        self.assertIn('current_user_background', result)
        self.assertIn('reply_to_user', result)
        self.assertIn('reply_to_message', result)

    def test_should_not_reply_happy_path(self):
        global_config.REPLY_CHANCE = 1  # any random number should satisfy
        self.assertFalse(self.users.should_not_reply())

    def test_should_not_reply_sad_path(self):
        global_config.REPLY_CHANCE = 0  # any random number should fail to reply
        self.assertTrue(self.users.should_not_reply())