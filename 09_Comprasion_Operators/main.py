"""Comparison operators are used to compare two values. They return a boolean value (True or False) based on the comparison."""

# Equal to (==)
print(5 == 5)  # True
print(5 == 3)  # False

# Not equal to (!=)
print(5 != 5)  # False
print(5 != 3)  # True

# Greater than (>)
print(5 > 3)  # True
print(3 > 5)  # False

# Less than (<)
print(3 < 5)  # True
print(5 < 3)  # False

# Greater than or equal to (>=)
print(5 >= 5)  # True
print(5 >= 3)  # True

# Less than or equal to (<=)
print(3 <= 5)  # True
print(5 <= 5)  # True

# Comparing strings
print("apple" == "apple")  # True
print("apple" == "orange")  # False
print("apple" > "orange")  # False (compares lexicographically)
print("orange" > "apple")  # True (compares lexicographically)

"""And/Or/not operators are used to combine multiple comparison expressions. They also return a boolean value based on the combined result."""\
# And operator (and)
print(5 > 3 and 3 > 1)  # True
print(5 > 3 and 1 > 3)  # False

# Or operator (or)
print(5 > 3 or 1 > 3)  # True
print(1 > 3 or 1 > 3)  # False

# Not operator (not)
print(not (5 > 3))  # False
print(not (1 > 3))  # True

print("apple" == "apple") # True (both are the same string)
print("5" == 5) # False (string vs integer)
print("5" == "5") # True (both are the same string)

