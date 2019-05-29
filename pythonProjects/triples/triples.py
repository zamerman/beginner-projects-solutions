import argparse
import json

text_path = "./json/text.json"
text_file = open(text_path, "r")
text = json.load(text_file)

def getSides():
    sides = []
    try:
        sides.append(float(input(text['prompt'].format('x'))))
        sides.append(float(input(text['prompt'].format('x'))))
        sides.append(float(input(text['prompt'].format('x'))))

        return sides

    except ValueError:
        print(text['value error'])
        return getSides()



def checkSides(sides):
    sq_sides = []

    for side in sides:
        sq_sides.append(side**2)

    if sq_sides[0] + sq_sides[1] == sq_sides[2]:
        print(text['true'])
    elif sq_sides[0] + sq_sides[2] == sq_sides[1]:
        print(text['true'])
    elif sq_sides[0] == sq_sides[1] + sq_sides[2]:
        print(text['true'])
    else:
        print(text['false'])


def tryAgain():
    response = input(text['try again'])

    if response == 'y':
        return True
    elif response == 'n':
        return False
    else:
        print(text['play again error'])
        return tryAgain()


def play():
    print(text['name'])

    sides = getSides()

    checkSides(sides)

    if tryAgain():
        play()


if __name__ == '__main__':
    play()
