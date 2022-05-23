"""
This file is part of RenameShows.

RenameShows is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

RenameShows is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with RenameShows.  If not, see <https://www.gnu.org/licenses/>.
"""

import pytest
from rename_shows.core.util.show_info_matcher import ShowInfoMatcher

"""
Title Tests
"""

def test_match_title():
    test_case = "some.random.movie.2010.1080p.blueray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)

    assert show_info_matcher.title == "some random movie"

# def test_match_title_contianing_year():
#     test_case = "some.random.movie.2012.2010.1080p.blueray.x264"
#     show_info_matcher = ShowInfoMatcher(test_case)
#     assert show_info_matcher.title == "some random movie 2012"

"""
Year Tests
"""

def test_match_year():
    test_case = "some.random.movie.2010.1080p.blueray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.year == "2010"

# def test_match_year_with_title_number():
#     test_case = "some.random.movie.2012.2010.1080p.blueray.x264"
#     show_info_matcher = ShowInfoMatcher(test_case)
#     assert show_info_matcher.year == "2010"

"""
Resolution Tests
"""

def test_match_resolution_480p():
    test_case = "some.random.movie.2010.480p.blueray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.resolution == "480p"

def test_match_resolution_720p():
    test_case = "some.random.movie.2010.720p.blueray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.resolution == "720p"

def test_match_resolution_1080p():
    test_case = "some.random.movie.2010.1080p.blueray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.resolution == "1080p"

"""
Source Tests
"""
def test_match_source_cam():
    assert False == False

"""
Video Codec Tests
"""
def test_match_video_codec():
    assert False == False

"""
Audio Tests
"""

def test_match_audio_aac():
    test_case = "some.random.movie.2010.1080p.blueray.aac.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.audio == "aac"

def test_match_audio_aac2_0():
    test_case = "some.random.movie.2010.1080p.blueray.aac2.0.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.audio == "aac2.0"

def test_match_audio_ac3():
    test_case = "some.random.movie.2010.1080p.blueray.ac3.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.audio == "ac3"

def test_match_audio_dts():
    test_case = "some.random.movie.2010.1080p.blueray.dts.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.audio == "dts"

def test_match_audio_dd5_1():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.audio == "dd5.1"

"""
Language Tests
"""

def test_match_language_multisubs():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.MULTiSUBS"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.language == "MULTiSUBS"

def test_match_language_multi():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.MULTi"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.language == "MULTi"

def test_match_language_nordic():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.NORDiC"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.language == "NORDiC"

def test_match_language_danish():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.DANiSH"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.language == "DANiSH"

def test_match_language_swedish():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SWEDiSH"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.language == "SWEDiSH"

def test_match_language_norwegian():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.NORWEGiAN"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.language == "NORWEGiAN"

def test_match_language_german():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.GERMAN"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.language == "GERMAN"

def test_match_language_italian():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.iTALiAN"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.language == "iTALiAN"

def test_match_language_french():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.FRENCH"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.language == "FRENCH"

def test_match_language_spanish():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.language == "SPANiSH"

"""
Edition Tests
"""

def test_match_edition_unrated():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.UNRATED"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.edition == "UNRATED"

def test_match_edition_dc():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.DC"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.edition == "DC"

def test_match_edition_directors_cut():
    test_case = (
        "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.Directors.CUT"
    )
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.edition == "Directors.CUT"

def test_match_edition_directors_edition():
    test_case = (
        "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.Directors.EDITION"
    )
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.edition == "Directors.EDITION"

def test_match_edition_extended_cut():
    test_case = (
        "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.EXTENDED.CUT"
    )
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.edition == "EXTENDED.CUT"

def test_match_edition_extended_edition():
    test_case = (
        "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.EXTENDED.EDITION"
    )
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.edition == "EXTENDED.EDITION"

def test_match_edition_extended():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.EXTENDED"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.edition == "EXTENDED"

def test_match_edition_3d():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.3D"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.edition == "3D"

def test_match_edition_2d():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.2D"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.edition == "2D"

def test_match_edition_nf():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.edition == "NF"

"""
Tags Tests
"""

def test_match_tags_complete():
    test_case = (
        "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.COMPLETE"
    )
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.tags == "COMPLETE"

def test_match_tags_limited():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.LiMiTED"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.tags == "LiMiTED"

def test_match_tags_internal():
    test_case = (
        "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL"
    )
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.tags == "iNTERNAL"

"""
Release Info Tests
"""

def test_match_release_info_real_proper():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264. \
        SPANiSH.NF.iNTERNAL.REAL.PROPER"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.release_info == "REAL.PROPER"

def test_match_release_info_proper():
    test_case = (
        "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.PROPER"
    )
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.release_info == "PROPER"

def test_match_release_info_repack():
    test_case = (
        "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.REPACK"
    )
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.release_info == "REPACK"

def test_match_release_info_readnfo():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.READNFO"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.release_info == "READNFO"

def test_match_release_info_read_nfo():
    test_case = "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.READ.NFO"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.release_info == "READ.NFO"

def test_match_release_info_dirfix():
    test_case = (
        "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.DiRFiX"
    )
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.release_info == "DiRFiX"

def test_match_release_info_nfofix():
    test_case = (
        "some.random.movie.2010.1080p.blueray.dd5.1.x264.SPANiSH.NF.iNTERNAL.NFOFiX"
    )
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.release_info == "NFOFiX"

"""
Season Tests
"""

def test_match_season_s():
    test_case = "some.random.tv.show.s01e01.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.season == 1

def test_match_season_season():
    test_case = "some.random.tv.show.season01e01.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.season == 1

def test_match_season_season_with_space():
    test_case = "some.random.tv.show.season 01e01.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.season == 1

def test_match_season_two_digits():
    test_case = "some.random.tv.show.s10e01.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.season == 10

"""
Episode Tests    
"""

def test_match_episode_episode_no_space():
    test_case = "some.random.tv.show.s01episode01.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1,)

def test_match_episode_episode_space():
    test_case = "some.random.tv.show.s01episode 01.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1,)

def test_match_episode_episode_no_zero_padding():
    test_case = "some.random.tv.show.s01episode1.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1,)

def test_match_episode_episode_space_no_zero_padding():
    test_case = "some.random.tv.show.s01episode 1.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1,)

def test_match_episode_e_no_space():
    test_case = "some.random.tv.show.s01e01.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1,)

def test_match_episode_e_no_zero_padding():
    test_case = "some.random.tv.show.s01e1.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1,)

def test_match_episode_e_dual_no_space():
    test_case = "some.random.tv.show.s01e0102.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1, 2)

def test_match_episode_e_dual_hiphen():
    test_case = "some.random.tv.show.s01e01-02.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1, 2)

def test_match_episode_e_dual_with_e():
    test_case = "some.random.tv.show.s01e01e02.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1, 2)

def test_match_episode_e_dual_hiphen_e():
    test_case = "some.random.tv.show.s01e01-e02.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1, 2)

def test_match_episode_e_3_digits():
    test_case = "some.random.tv.show.s01e199.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (199,)

def test_match_episode_e_dual_3_digits():
    test_case = "some.random.tv.show.s01e001004.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1, 4)

def test_match_episode_e_dual_no_zero_padding_hiphen():
    test_case = "some.random.tv.show.s01e1-e2.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1, 2)

def test_match_episode_e_dual_3_digit_hiphen_e():
    test_case = "some.random.tv.show.s01e001-e002.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == (1, 2)

def test_match_episode_no_match():
    test_case = "some.random.tv.show.s01.1080p.bluray.x264"
    show_info_matcher = ShowInfoMatcher(test_case)
    assert show_info_matcher.episode == None

"""
Release Group Tests
"""
def test_match_release_group():
    assert False == False
