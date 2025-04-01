from example import *
from unittest import TestCase


class TestMethods(TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)

    def test_add(self):
        self.assertEqual(add(1, 2), 3)


