import unittest

from classes.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Scott")

    def test_guest_has_name(self):
        self.assertEqual("Scott", self.guest.name)
