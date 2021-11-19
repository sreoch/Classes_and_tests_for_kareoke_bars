import unittest

from classes.guest import Guest
from classes.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Scott", 40)
        self.guest_1 = Guest("Joe", 10)
        self.room = Room(10, 1, 20)

    def test_guest_has_name(self):
        self.assertEqual("Scott", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(40, self.guest.money)

    def test_guest_buy_room(self):
        self.guest.buy_room(self.room.room_cost)
        self.assertEqual(20, self.guest.money)

    def test_guest_cant_afford_room(self):
        self.assertEqual(
            "You cannot afford this room", self.guest_1.buy_room(self.room.room_cost)
        )
