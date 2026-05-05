"""Dunder methods --> Double Underscore Methods
Dunder methods are special methods in Python that have double underscores before and after their names. They are also known as magic methods or special methods. Dunder methods allow you to define the behavior of your objects in various situations, such as when they are printed, compared, or called. Some common dunder methods include:
"""


class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} is your name and your marks are {self.marks}"


obj = Students("Rohit", 98)

print(obj)


class Shopping:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


obj = Shopping(["apple", "milk", "bread"])
obj2 = Shopping(["apple", "orange", "banana", "choclate"])

print(len(obj2))


class Numbers:
    def __init__(self, number):
        self.number = number

    def __add__(self, custom):
        return self.number + custom.number


obj1 = Numbers(1)
obj2 = Numbers(6)

print(obj1 + obj2)
