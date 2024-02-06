class Customer:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception
        
    def orders(self): #, new_order=None):
        from classes.order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self): #, new_coffee=None):
        #from classes.coffee import Coffee
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        from classes.order import Order
        Order(self, coffee, price)