import unittest
from io_helper.io_helper import *
import os


class Case(unittest.TestCase):

    def setUp(self):
        self.dir_path = os.path.dirname(os.path.abspath(__file__))

    def test_get_setting_returns_a_string(self):
        path = os.path.join(self.dir_path, "test_setting.txt")
        result = file_to_string(path)
        self.assertEqual(result, "this is a test setting\nit is a cool setting")

    def test_minify_string_two(self):
        s = "a\n\nb  c"
        result = minify_string(s)
        self.assertEqual(result, "a\nb c")

    def test_minify_string_three(self):
        s = "a\n\n\nb   c"
        result = minify_string(s)
        self.assertEqual(result, "a\nb c")

    def test_minify_string_single(self):
        s = "a\nb c"
        result = minify_string(s)
        self.assertEqual(result, "a\nb c")

    def test_minify_string_semicolon(self):
        s = "a; b"
        result = minify_string(s)
        self.assertEqual(result, "a;b")

    def test_minify_string_comma(self):
        s = "a, b"
        result = minify_string(s)
        self.assertEqual(result, "a,b")

    def test_minify_string_colon(self):
        s = "a: b"
        result = minify_string(s)
        self.assertEqual(result, "a:b")