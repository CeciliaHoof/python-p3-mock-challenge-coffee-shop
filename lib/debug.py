#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    coffee = Coffee("Hazelnut Latte")
    coffee_2 = Coffee("Mocha")
    
    customer = Customer("Steve")
    customer_2 = Customer("Bob")
    
    order_1 = Order(customer, coffee, 2)
    order_2 = Order(customer, coffee, 5)
    order_3 = Order(customer, coffee_2, 5)
    order_4 = Order(customer_2, coffee, 2)
    order_5 = Order(customer_2, coffee_2, 3)
    order_6 = Order(customer_2, coffee_2, 5)

    ipdb.set_trace()
