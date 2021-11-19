import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(10)
        self.guest_1 = Guest("Cameron")
        self.guest_2 = Guest("Scott")
        self.guest_3 = Guest("Matthew")
        self.song_1 = Song('Japan', 'Yot Club')

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room.capacity)

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
