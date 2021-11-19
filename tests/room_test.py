import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(10, 1, 20)
        self.guest_1 = Guest("Cameron", 10)
        self.guest_2 = Guest("Scott", 50)
        self.guest_3 = Guest("Matthew", 100)
        self.song_1 = Song("Japan", "Yot Club")

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room.capacity)

    def test_room_has_cost(self):
        self.assertEqual(20, self.room.room_cost)

    def test_room_can_add_guest_to_list(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room.current_guests))

    def test_room_can_remove_guest_from_list(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.room.check_out_guest(self.guest_2)
        self.assertEqual(1, len(self.room.current_guests))

    def test_can_add_song_to_room(self):
        self.room.add_to_playlist(self.song_1)
        self.assertEqual(1, len(self.room.playlist))

    def test_room_wont_allow_over_capacity(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)
        self.room.check_in_guest(self.guest_2)
        self.assertEqual("Room capacity is 10", self.room.check_in_guest(self.guest_1))

