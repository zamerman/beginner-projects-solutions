#!/usr/bin/env python
## Imports
import json

## Data Loader
data_path = "./json/data.json"
data = json.load(open(data_path, 'r'))

## Text Variables
error_message = '''At least one of your coin weights is not a floating point number.'''

## Program Intro
print('\nCoin Estimator by Weight')

## Units Selector
units = ''
while units != 'g' and units != 'lb':
    units = input('\nSelect Units; (g/lb): ')
    if units != 'g' and units != 'lb':
        print('{0} is not a valid unit.'.format(units))

## Weight Input
coins = {'pennies': 0, 'nickels': 0, 'dimes': 0, 'quarters': 0}
weights_are_valid = False
while not weights_are_valid:
    print("\nWeight({0})".format(units))
    coins['pennies'] = input('Pennies: ')
    coins['nickels'] = input('Nickels: ')
    coins['dimes'] = input('Dimes: ')
    coins['quarters'] = input('Quarters: ')

    ## Iterate Through Weights to Convert to Float Values
    try:
        for key in coins.keys():
            coins[key] = float(coins[key])
    except ValueError:
        print(error_message)

    for key in coins.keys():
        if coins[key] >= 0:
            weights_are_valid = True
        else:
            print("The weight for {} must be positive.".format(key))

## Calculate Number of Coins
print("\nCoin Counts")
for key in coins.keys():
    coins[key] = int(round(coins[key]/data['coin_weights'][units][key], 0))
    print("{}: {}".format(key, coins[key]))

## Calculate Number of Coin Wrappers
print("\nCoin Wrapper Counts")
for key in coins.keys():
    coins[key] = int(coins[key]/data['coin_wrappers'][key])
    print("wrappers for {}: {}".format(key, coins[key]))
