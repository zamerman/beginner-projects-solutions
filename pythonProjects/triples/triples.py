import argparse
import json

text_path = "./json/text.json"
text_file = open(text_path, "r")
text_dictionary = json.load(text_file)

print(text_dictionary['name'])
x = int(input(text_dictionary['prompt'].format('x')))
y = int(input(text_dictionary['prompt'].format('y')))
z = int(input(text_dictionary['prompt'].format('z')))
print([x, y, z])
