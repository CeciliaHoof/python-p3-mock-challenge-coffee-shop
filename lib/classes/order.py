

class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        self.__class__.all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,val):
        if type(val) == int and 0 < val < 11:
            self._price = val
        else:
            raise Exception("invalid price")