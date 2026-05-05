"""Strings are a sequence of characters. They are immutable, which means that once a string is created, it cannot be changed. However, you can create a new string by concatenating two or more strings together."""

a = "Hello"
print(a[1]);

b="Rohit Yadav"
print(b[0:8]) # slicing

c="Hello World"
print(c[1:10:2]) # slicing with step. The first number is the starting index, the second number is the ending index, and the third number is the step. In this case, it will print every second character from index 1 to index 5.

d = "hello I am Rohit Yadav"
print(d[0:5])
print(d[11:16])
print(d[17:22])


age = 22
Des = "Developer"
print(f"My name is Rohit Yadav, I am {age} years old and I am a {Des}.") # f-string