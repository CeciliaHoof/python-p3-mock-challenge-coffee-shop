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
        pass
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        pass