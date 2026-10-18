#!/usr/bin/env python3

class Coffee:
    SIZES = ["Small", "Medium", "Large"]

    def __init__(self, size="Medium", price=3.0):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in Coffee.SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)):
            self._price = value
        else:
            print("price must be a number")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1