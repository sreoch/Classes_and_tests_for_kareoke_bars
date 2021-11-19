import unittest

from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Not Allowed", "TV Girl")

    def test_song_has_name(self):
        self.assertEqual("Not Allowed", self.song.song_name)

    def test_song_has_artis(self):
        self.assertEqual("TV Girl", self.song.artist)
