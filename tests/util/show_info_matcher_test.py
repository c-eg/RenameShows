import unittest
from cgi import test

from rename_shows.util.show_info_matcher import ShowInfoMatcher


class TestShowInfoMatcher(unittest.TestCase):
    """
    Unit test class to test ShowInfoMatcher in rename_shows/util/show_info_matcher.
    """
    def test_match_title(self):
        self.assertTrue(False)

    def test_match_year(self):
        test_case = "some.random.movie.2010.1080p.blueray.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "2010"

        self.assertEqual(show_info_matcher.year, expected_result)

    def test_match_resolution_480p(self):
        test_case = "some.random.movie.2010.480p.blueray.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "480p"

        self.assertEqual(show_info_matcher.resolution, expected_result)

    def test_match_resolution_720p(self):
        test_case = "some.random.movie.2010.720p.blueray.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "720p"

        self.assertEqual(show_info_matcher.resolution, expected_result)

    def test_match_resolution_1080p(self):
        test_case = "some.random.movie.2010.1080p.blueray.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "1080p"

        self.assertEqual(show_info_matcher.resolution, expected_result)

    def test_match_source(self):
        self.assertTrue(False)

    def test_match_video_codec(self):
        self.assertTrue(False)

    def test_match_audio(self):
        self.assertTrue(False)

    def test_match_language(self):
        self.assertTrue(False)

    def test_match_edition(self):
        self.assertTrue(False)

    def test_match_tags(self):
        self.assertTrue(False)

    def test_match_release_info(self):
        self.assertTrue(False)

    def test_match_season(self):
        self.assertTrue(False)

    def test_match_episode(self):
        self.assertTrue(False)

    def test_match_release_group(self):
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
