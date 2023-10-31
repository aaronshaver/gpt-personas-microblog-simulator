import unittest
from worker.worker import Worker
import os


class Case(unittest.TestCase):

    def setUp(self):
        self.worker = Worker()
        self.dir_path = os.path.dirname(os.path.abspath(__file__))

    def test_get_setting_returns_a_string(self):
        path = os.path.join(self.dir_path, "test_setting.txt")
        setting = self.worker.get_setting(path)
        self.assertEqual(setting, "this is a test setting\nit is a cool setting")
