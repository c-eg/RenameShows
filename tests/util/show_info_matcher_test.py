import unittest

from rename_shows.util.show_info_matcher import ShowInfoMatcher


class TestShowInfoMatcher(unittest.TestCase):
    """
    Unit test class to test ShowInfoMatcher in rename_shows/util/show_info_matcher.
    """

    """
    Title Tests
    """
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

    """
    Year Tests
    """
    def test_match_year(self):
        test_case = "some.random.movie.2010.1080p.blueray.x264"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "2010"

        self.assertEqual(show_info_matcher.year, expected_result)

    """
    Resolution Tests
    """
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

    """
    Source Tests
    """
    # def test_match_source_cam(self):
    #     self.assertTrue(False)

    """
    Video Codec Tests
    """
    # def test_match_video_codec(self):
    #     self.assertTrue(False)

    """
    Audio Tests
    """
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

    """
    Language Tests
    """
    def test_match_language_multisubs(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.MULTiSUBS"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "MULTiSUBS"

        self.assertEqual(show_info_matcher.language, expected_result)

    def test_match_language_multi(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.MULTi"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "MULTi"

        self.assertEqual(show_info_matcher.language, expected_result)

    def test_match_language_nordic(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.NORDiC"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "NORDiC"

        self.assertEqual(show_info_matcher.language, expected_result)

    def test_match_language_danish(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.DANiSH"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "DANiSH"

        self.assertEqual(show_info_matcher.language, expected_result)

    def test_match_language_swedish(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SWEDiSH"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "SWEDiSH"

        self.assertEqual(show_info_matcher.language, expected_result)

    def test_match_language_norwegian(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.NORWEGiAN"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "NORWEGiAN"

        self.assertEqual(show_info_matcher.language, expected_result)

    def test_match_language_german(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.GERMAN"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "GERMAN"

        self.assertEqual(show_info_matcher.language, expected_result)

    def test_match_language_italian(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.iTALiAN"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "iTALiAN"

        self.assertEqual(show_info_matcher.language, expected_result)

    def test_match_language_french(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.FRENCH"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "FRENCH"

        self.assertEqual(show_info_matcher.language, expected_result)

    def test_match_language_spanish(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "SPANiSH"

        self.assertEqual(show_info_matcher.language, expected_result)

    """
    Edition Tests
    """
    def test_match_edition_unrated(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.UNRATED"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "UNRATED"

        self.assertEqual(show_info_matcher.edition, expected_result)

    def test_match_edition_dc(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.DC"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "DC"

        self.assertEqual(show_info_matcher.edition, expected_result)

    def test_match_edition_directors_cut(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.Directors.CUT"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "Directors.CUT"

        self.assertEqual(show_info_matcher.edition, expected_result)

    def test_match_edition_directors_cut(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.Directors.EDITION"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "Directors.EDITION"

        self.assertEqual(show_info_matcher.edition, expected_result)

    def test_match_edition_extended_cut(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.EXTENDED.CUT"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "EXTENDED.CUT"

        self.assertEqual(show_info_matcher.edition, expected_result)

    def test_match_edition_extended_edition(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.EXTENDED.EDITION"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "EXTENDED.EDITION"

        self.assertEqual(show_info_matcher.edition, expected_result)

    def test_match_edition_extended(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.EXTENDED"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "EXTENDED"

        self.assertEqual(show_info_matcher.edition, expected_result)

    def test_match_edition_3d(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.3D"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "3D"

        self.assertEqual(show_info_matcher.edition, expected_result)

    def test_match_edition_2d(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.2D"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "2D"

        self.assertEqual(show_info_matcher.edition, expected_result)

    def test_match_edition_nf(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "NF"

        self.assertEqual(show_info_matcher.edition, expected_result)

    """
    Tags Tests
    """
    def test_match_tags_complete(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.COMPLETE"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "COMPLETE"

        self.assertEqual(show_info_matcher.tags, expected_result)

    def test_match_tags_limited(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.LiMiTED"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "LiMiTED"

        self.assertEqual(show_info_matcher.tags, expected_result)

    def test_match_tags_internal(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "iNTERNAL"

        self.assertEqual(show_info_matcher.tags, expected_result)

    """
    Release Info Tests
    """
    def test_match_release_info_real_proper(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.REAL.PROPER"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "REAL.PROPER"

        self.assertEqual(show_info_matcher.release_info, expected_result)

    def test_match_release_info_proper(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.PROPER"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "PROPER"

        self.assertEqual(show_info_matcher.release_info, expected_result)

    def test_match_release_info_repack(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.REPACK"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "REPACK"

        self.assertEqual(show_info_matcher.release_info, expected_result)

    def test_match_release_info_readnfo(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.READNFO"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "READNFO"

        self.assertEqual(show_info_matcher.release_info, expected_result)

    def test_match_release_info_read_nfo(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.READ.NFO"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "READ.NFO"

        self.assertEqual(show_info_matcher.release_info, expected_result)

    def test_match_release_info_dirfix(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.DiRFiX"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "DiRFiX"

        self.assertEqual(show_info_matcher.release_info, expected_result)

    def test_match_release_info_nfofix(self):
        test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.NFOFiX"
        show_info_matcher = ShowInfoMatcher(test_case)
        expected_result = "NFOFiX"

        self.assertEqual(show_info_matcher.release_info, expected_result)

    """
    Season Tests
    """
    # def test_match_season(self):
    #     self.assertTrue(False)

    """
    Episode Tests
    """
    # def test_match_episode(self):
    #     self.assertTrue(False)

    """
    Release Group Tests
    """
    # def test_match_release_group(self):
    #     self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
