class Coins:
    '''A class which contains US coins'''

    def __init__(self, quarters=0, dimes=0, nickels=0, pennies=0):
        self.quarters = quarters
        self.dimes = dimes
        self.nickels = nickels
        self.pennies = pennies

    def setQ(self, quarters):
        self.quarters = quarters

    def setD(self, dimes):
        self.dimes = dimes

    def setN(self, nickels):
        self.nickels = nickels

    def setP(self, pennies):
        self.pennies = pennies

    def incQ(self):
        self.quarters += 1

    def incD(self):
        self.dimes += 1

    def incN(self):
        self.nickels += 1

    def incP(self):
        self.pennies += 1

    def getQ(self):
        return self.quarters

    def getD(self):
        return self.dimes

    def getN(self):
        return self.nickels

    def getP(self):
        return self.pennies
