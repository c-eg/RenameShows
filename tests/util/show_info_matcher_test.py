import unittest

from rename_shows.util.show_info_matcher import ShowInfoMatcher


class TestShowInfoMatcher(unittest.TestCase):

    def setUp(self):
        self.show_info_matches = ShowInfoMatcher("First.Man.2018.1080p.BluRay.REMUX.AVC.Atmos-EPSiLON.torrent")
        # pass

    def test_title_match(self):
        self.assertEqual(self.show_info_matches.title, "First Man")

if __name__ == "__main__":
    unittest.main()
