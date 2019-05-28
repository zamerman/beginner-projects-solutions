#!/usr/bin/python

class BeerOnTheWall:
    """A class which tells you how much beer is on the wall"""
    def __init__(self, beer):
        self.__beer = beer

    def howMuchBeer(self):
        return self.__beer

    def howManyBottles(self):
        return TopLyrics(self.__beer)

    def takeOneDown(self):
        self.__beer -= 1
        return BottomLyrics(self.__beer)


def howManyBottles(beer):
    commonLyrics = "{0} bottles of beer"
    singularLyrics = "{0} bottle of beer"

    lyrics = ""

    if beer == 1:
        lyrics += singularLyrics.format(beer)
    else:
        lyrics += commonLyrics.format(beer)

    return lyrics


def TopLyrics(beer):
    lyrics = ""

    lyrics += howManyBottles(beer) + " on the wall, "
    lyrics += howManyBottles(beer) + ","

    return lyrics


def BottomLyrics(beer):
    lyrics = ""

    lyrics += "take one down, pass it around, "
    lyrics += howManyBottles(beer) + " on the wall.\n"

    return lyrics


def main():
    beer = BeerOnTheWall(99)
    while beer.howMuchBeer() > 0:
        print(beer.howManyBottles())
        print(beer.takeOneDown())


if __name__ == "__main__":
    main()
