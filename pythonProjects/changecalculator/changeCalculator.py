from coins import Coins

returnForm = "\nChange: {}\n\nQuarters: {}\nDimes: {}\nNickels: {}\nPennies: {}"

def getInput():
    return input("float Change/float Payment,Price/str q:")

def parseResponse(inputString):
    if str(inputString).find(',') == -1:
        change = float(inputString)
        return change
    else:
        payment, price = str(inputString).split(',')
        payment = float(payment)
        price = float(price)
        change = payment - price
        return change

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
    if inputString == 'q':
        return
    change = parseResponse(inputString)
    coins = calculateChange(change)
    print(returnForm.format(str(change),
                            coins.getQ(),
                            coins.getD(),
                            coins.getN(),
                            coins.getP()))
    main()


main()
