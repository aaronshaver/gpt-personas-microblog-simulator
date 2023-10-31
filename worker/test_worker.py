import unittest
from worker.worker import Worker


class Case(unittest.TestCase):

    def setUp(self):
        self.worker = Worker()

    def test_get_setting_returns_a_string(self):
        result = self.worker.get_setting()
        self.assertTrue(len(result) > 0)

    def test_get_rules(self):
        result = self.worker.get_rules()
        self.assertTrue(len(result) > 0)

    def test_get_rules(self):
        result = self.worker.get_tone()
        self.assertTrue(len(result) > 0)

    def test_get_system_content(self):
        result = self.worker.get_system_content()
        self.assertTrue("tone" in result)
        self.assertTrue("setting" in result)
        self.assertTrue("rules" in result)