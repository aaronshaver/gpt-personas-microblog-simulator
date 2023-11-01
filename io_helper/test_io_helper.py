import unittest
from io_helper.io_helper import file_to_string
import os


class Case(unittest.TestCase):

    def setUp(self):
        self.dir_path = os.path.dirname(os.path.abspath(__file__))

    def test_get_setting_returns_a_string(self):
        path = os.path.join(self.dir_path, "test_setting.txt")
        result = file_to_string(path)
        self.assertEqual(result, "this is a test setting\nit is a cool setting")
