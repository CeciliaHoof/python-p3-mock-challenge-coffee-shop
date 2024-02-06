
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
    def price(self, new_price):
        if type(new_price) == int and 1 <= new_price <= 10:
            self._price = new_price
        else:
            raise Exception
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from classes.customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise Exception
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from classes.coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise Exception