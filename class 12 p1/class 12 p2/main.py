class Computer:
    def __init__(self):
        self.maxprince = 1000

    def sell(self):
        print("Selling price:{}".format(self.maxprice))

    def setmaxprice(self,price):
        self.maxprice = price

c = Computer()

c.maxprice = 1000
c.sell()

c.setmaxprice = 1500
c.sell()
