from coins import Coins
import sys

returnForm = "\nChange: {}\n\nQuarters: {}\nDimes: {}\nNickels: {}\nPennies: {}"


def checkArgs(func):
    def inside():
        if len(sys.argv) != 2:
            print("Must insert argument")
            return
        return func()
    return inside


def checkChange(func):
    def inside():
        try:
            float(sys.argv[1])
        except ValueError:
            print("Argument must be float castable")
            return
        if sys.argv[1].find('.') + 3 != len(sys.argv[1]):
            print("There must be two numbers after the decimal point")
            return
        return func()
    return inside


@checkArgs
@checkChange
def getArgs():
    return float(sys.argv[1])


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
    args = getArgs()
    change = calculateChange(args)
    print(returnForm.format(args,
                            change.getQ(),
                            change.getD(),
                            change.getN(),
                            change.getP()))


main()
