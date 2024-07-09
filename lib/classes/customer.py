class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        if type(val) == str and 0 < len(val) < 16:
            self._name = val
        else:
            raise Exception("Invalid name")
        
    def orders(self, new_order=None):
        from classes.order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self, new_coffee=None):
        return set(list(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        from classes.order import Order
        Order(self, coffee, price)