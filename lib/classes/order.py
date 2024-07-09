

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
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, val):
        from classes.customer import Customer
        if isinstance(val, Customer):
            self._customer = val
        else:
            raise Exception("invalid customer")
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, val):
        from classes.coffee import Coffee
        if isinstance(val, Coffee):
            self._coffee = val
        else:
            raise Exception("invalid coffee")