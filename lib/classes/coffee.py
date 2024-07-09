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
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass