from util.show_info_matcher import ShowInfoMatcher


def main():
    test = ShowInfoMatcher("The.Good.Place.S04E11.1080p.NF.WEB-DL.DDP5.1.x264-AJP69")
    print(test.title)
    print(test.year)
    print(test.resolution)

    test = ShowInfoMatcher("First.Man.2018.1080p.BluRay.REMUX.AVC.Atmos-EPSiLON.torrent")
    print(test.title)
    print(test.year)
    print(test.resolution)


if __name__ == "__main__":
    main()
