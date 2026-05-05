"""inputs are stored in variables as strings, so we need to convert them to the appropriate data type if necessary. In this example, we will keep the age as a string for simplicity."""

name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")
print(type(age))

# If you want to convert the age to an integer, you can do it like this:
name2 = input("Enter your name: ")
age2 = int(input("Enter your age: "))
print(f"Hello, {name2}! You are {age2} years old.")
print(type(age2))