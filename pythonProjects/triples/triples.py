import argparse
import json

text_path = "./json/text.json"
text_file = open(text_path, "r")
text_dictionary = json.load(text_file)

play = True
while play:
    print(text_dictionary['name'])

    sides = []
    sides.append(int(input(text_dictionary['prompt'].format('x'))))
    sides.append(int(input(text_dictionary['prompt'].format('y'))))
    sides.append(int(input(text_dictionary['prompt'].format('z'))))

    sq_sides = []
    for side in sides:
        sq_sides.append(side**2)

    triple = False
    if sq_sides[0] + sq_sides[1] == sq_sides[2]:
        triple = True
    elif sq_sides[0] + sq_sides[2] == sq_sides[1]:
        triple = True
    elif sq_sides[0] == sq_sides[1] + sq_sides[2]:
        triple = True

    if triple:
        print(text_dictionary['true'])
    else:
        print(text_dictionary['false'])

    redo = ""
    while (redo != 'r') and (redo != 'q'):
        print(text_dictionary['try again'])
        redo = input()

    if redo == 'q':
        play = False
