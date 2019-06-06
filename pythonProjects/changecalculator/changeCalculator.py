from coins import Coins
import sys

returnForm = "\nChange: {}\n\nQuarters: {}\nDimes: {}\nNickels: {}\nPennies: {}"


def getInput():
    return input("Change/Payment,Price:")


def calculateChange(change):
    '''Calculates the coins for the change and returns it as an object of the
    Coins class

    Parameters
    change - a floating point two decimal number representing the dollars that
        need to be represented as coins'''

    coins = Coins()

    while change > 0:
        if change > 0.25:
            coins.incQ()
            change -= 0.25
        elif change > 0.10:
            coins.incD()
            change -= 0.10
        elif change > 0.05:
            coins.incN()
            change -= 0.05
        else:
            coins.incP()
            change -= 0.01

    return coins


def main():
    print("\nChange Calculator")
    inputString = str(getInput())
    change = calculateChange(args)
    print(returnForm.format(args,
                            change.getQ(),
                            change.getD(),
                            change.getN(),
                            change.getP()))


main()
