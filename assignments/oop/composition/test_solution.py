import unittest
from solution import Playlist, Song

class PlaylistTests(unittest.TestCase):
    def test_empty_playlist(self):
        playlist = Playlist("Focus")
        self.assertEqual(playlist.name, "Focus")
        self.assertEqual(playlist.duration(), 0)

    def test_adds_songs_and_totals_duration(self):
        playlist = Playlist("Focus")
        first = Song("Alpha", 120)
        second = Song("Beta", 75)
        playlist.add(first)
        playlist.add(second)
        self.assertEqual(playlist.songs, [first, second])
        self.assertEqual(playlist.duration(), 195)

if __name__ == "__main__":
    unittest.main()
