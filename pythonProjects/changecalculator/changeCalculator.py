from coins import Coins

returnForm = "\nChange: {}\n\nQuarters: {}\nDimes: {}\nNickels: {}\nPennies: {}"

def getChange():
    response = input("float Change/float Payment,float Price/str q:")

    if response == 'q':
        exit()

    if response.find(',') == -1:
        response = response
    else:
        response = response.split(',')

    if isinstance(response, list):
        if False in [checkDecimal(item) for item in response]:
            print("Responses must have two decimal places")
            return getChange()
        else:
            response = round(float(response[0]) - float(response[1]), 2)
            return response
    else:
        if not checkDecimal(response):
            print("Response must have two decimal places")
            return getChange()
        else:
            return float(response)


def checkDecimal(string):
    if string.count('.') == 0 or string.count('.') > 1:
        return False
    else:
        decimalPlaces = string[string.find('.'):]
        if len(decimalPlaces) == 3:
            return True
        else:
            return False


def calculateChange(change):
    '''Calculates the coins for the change and returns it as an object of the
    Coins class

    Parameters
    change - a floating point two decimal number representing the dollars that
        need to be represented as coins'''

    coins = Coins()

    while change >= 0.25:
        coins.incQ()
        change = round(change - 0.25, 2)

    while change >= 0.1:
        coins.incD()
        change = round(change - 0.1, 2)

    while change >= 0.05:
        coins.incN()
        change = round(change - 0.05, 2)

    while change >= 0.01:
        coins.incD()
        change = round(change - 0.01, 2)

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
