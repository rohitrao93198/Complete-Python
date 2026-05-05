"""Data types in Python -- int, float, str, bool, list, tuple, set, dict"""
"""Data types are the different types of values that can be stored and manipulated in a programming language. In Python, there are several built-in data types, including:"""

"""1. int: Represents integer values, such as 1, 2, 3, etc."""
a = 10
b = -5
print(type(a))

"""2. float: Represents floating-point numbers, such as 3.14, 2.718, etc."""
c = 3.14
d = -2.718
print(type(c))

"""3. str: Represents strings, which are sequences of characters, such as "Hello", "Python", etc."""
name = "Hello, World!"
print(type(name))

"""4. bool: Represents boolean values, which can be either True or False."""
is_valid = True
is_empty = False
print(type(is_valid))

"""5. list: Represents a collection of ordered, mutable, and heterogeneous elements, such as [1, 2, 3], ["apple", "banana", "cherry"], etc."""
fruits = ["apple", "banana", "cherry"]
print(type(fruits))

"""6. tuple: Represents a collection of ordered, immutable, and heterogeneous elements, such as (1, 2, 3), ("apple", "banana", "cherry"), etc."""
coordinates = (10, 20)
print(type(coordinates))


"""7. set: Represents a collection of unordered, mutable, and unique elements, such as {1, 2, 3}, {"apple", "banana", "cherry"}, etc."""
unique_numbers = {1, 2, 3, 4, 5}
print(type(unique_numbers))


"""8. dict: Represents a collection of key-value pairs, where each key is unique and maps to a value, such as {"name": "Alice", "age": 30}, {"fruit": "apple", "color": "red"}, etc."""
person = {"name": "Alice", "age": 30}
print(type(person))
