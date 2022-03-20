import unittest

from rename_shows.util.show_info_matcher import ShowInfoMatcher


class TestShowInfoMatcher(unittest.TestCase):
    """
    Unit test class to test ShowInfoMatcher in rename_shows/util/show_info_matcher.
    """

    """Title Tests"""
    def test_match_title(self):
        test_case = "some.random.movie.2010.1080p.blueray.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "some random movie"

        self.assertEqual(show_info_matcher.title, expected_result, "")

    def test_match_title_contianing_year(self):
        test_case = "some.random.movie.2012.2010.1080p.blueray.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "some random movie 2012"

        self.assertEqual(show_info_matcher.title, expected_result)

    """Year Tests"""
    def test_match_year(self):
        test_case = "some.random.movie.2010.1080p.blueray.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "2010"

        self.assertEqual(show_info_matcher.year, expected_result)

    """Resolution Tests"""
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

    """Source Tests"""
    # def test_match_source_cam(self):
    #     self.assertTrue(False)

    # """Video Codec Tests"""
    # def test_match_video_codec(self):
    #     self.assertTrue(False)

    """Audio Tests"""
    def test_match_audio_aac(self):
        test_case = "some.random.movie.2010.1080p.blueray.aac.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "aac"

        self.assertEqual(show_info_matcher.audio, expected_result)

    def test_match_audio_aac2_0(self):
        test_case = "some.random.movie.2010.1080p.blueray.aac2.0.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "aac2.0"

        self.assertEqual(show_info_matcher.audio, expected_result)

    def test_match_audio_ac3(self):
        test_case = "some.random.movie.2010.1080p.blueray.ac3.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "ac3"

        self.assertEqual(show_info_matcher.audio, expected_result)

    def test_match_audio_dts(self):
        test_case = "some.random.movie.2010.1080p.blueray.dts.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "dts"

        self.assertEqual(show_info_matcher.audio, expected_result)

    def test_match_audio_dd5_1(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "dd5.1"

        self.assertEqual(show_info_matcher.audio, expected_result)

    """Language Tests"""
    # def test_match_language(self):
    #     self.assertTrue(False)

    """Edition Tests"""
    # def test_match_edition(self):
    #     self.assertTrue(False)

    """Tags Tests"""
    # def test_match_tags(self):
    #     self.assertTrue(False)

    """Release Info Tests"""
    # def test_match_release_info(self):
    #     self.assertTrue(False)

    """Season Tests"""
    # def test_match_season(self):
    #     self.assertTrue(False)

    """Episode Tests"""
    # def test_match_episode(self):
    #     self.assertTrue(False)

    """Release Group Tests"""
    # def test_match_release_group(self):
    #     self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
