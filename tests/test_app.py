import unittest

from src.app import add


class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,2), 3)