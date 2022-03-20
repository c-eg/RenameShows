import unittest

from rename_shows.util.show_info_matcher import ShowInfoMatcher


class TestShowInfoMatcher(unittest.TestCase):

    def test_match_title(self):
        self.assertEqual(False)

    def test_match_year(self):
        self.assertEqual(False)

    def test_match_resolution(self):
        self.assertEqual(False)

    def test_match_source(self):
        self.assertEqual(False)

    def test_match_video_codec(self):
        self.assertEqual(False)

    def test_match_audio(self):
        self.assertEqual(False)

    def test_match_language(self):
        self.assertEqual(False)

    def test_match_edition(self):
        self.assertEqual(False)

    def test_match_tags(self):
        self.assertEqual(False)

    def test_match_release_info(self):
        self.assertEqual(False)

    def test_match_season(self):
        self.assertEqual(False)

    def test_match_episode(self):
        self.assertEqual(False)

    def test_match_release_group(self):
        self.assertEqual(False)

if __name__ == "__main__":
    unittest.main()
