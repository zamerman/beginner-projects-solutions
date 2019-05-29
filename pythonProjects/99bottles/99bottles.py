#!/usr/env/bash python

verse = "{} of beer on the wall, {} of beer.\nTake one down, pass it around, {} of beer on the wall."
end_verse = "No more bottles of beer on the wall, no more bottles of beer.\nGo to the stare and by some more, {} of beer on the wall."

def bottles(n):
    if n == 1:
        return "{} bottle".format(n)
    else:
        return "{} bottles".format(n)

def lyrics(n):
    if n == 0:
        print(end_verse.format(99))
    else:
        print(verse.format(bottles(n), bottles(n), bottles(n - 1))
        lyrics(n - 1)

if __name__ == "__main__":
    lyrics()
