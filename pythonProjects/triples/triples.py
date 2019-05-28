import argparse
import json

text_path = "./json/text.json"
text_file = open(text_path, "r")
text_dictionary = json.load(text_file)

print(text_dictionary['name'])

sides = []
sides.append(int(input(text_dictionary['prompt'].format('x'))))
sides.append(int(input(text_dictionary['prompt'].format('y'))))
sides.append(int(input(text_dictionary['prompt'].format('z'))))

print(sides)
