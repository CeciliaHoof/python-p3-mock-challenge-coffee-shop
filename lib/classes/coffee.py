class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        if not hasattr(self, "name"):
            self._name = val
        else:
            raise Exception("Invalid name")
            
    def orders(self, new_order=None):
        from classes.order import Order
        pass
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass