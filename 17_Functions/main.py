"""Functions are reusable blocks of code that perform a specific task. They allow you to break down your code into smaller, more manageable pieces, and can be called multiple times throughout your program. In Python, you can define a function using the `def` keyword, followed by the function name and parentheses. You can also specify parameters inside the parentheses, which are used to pass values to the function."""

"""****************Without functions**********************"""
# num1 = input("Enter the number: ")
# num2 = input("Enter the number: ")

# result = int(num1) + int(num2)
# print("The sum is:", result)


# def add_numbers(num1, num2):
#     return num1 + num2


"""*************With functions**********************"""
# number1 = int(input("Enter the number: "))
# number2 = int(input("Enter the number: "))

# result = add_numbers(number1, number2)
# print("The sum is:", result)


# def greet():
#     return "Hello World"

# print(greet())


# def add(a, b):
#     return a + b

# result = add(10, 20)
# print(result)


# Question - check the no is palindrome or not
# def pallindrome(x):
#     rev = 0
#     copy = x
#     while x > 0:
#         rev = (rev * 10) + (x % 10)
#         x = x // 10

#     if rev == copy:
#         return True
#     else:
#         return False


# print(pallindrome(121))


# keyword argument
# def addition(a, b):
#     print(a + b)


# addition(b=12, a=8)


# def add(a, b, c):
#     print(a + b + c)


# add(12, c=10, b=8)


# Default argument
# def add(a, b, c=13):
#     print(a + b + c)


# add(12, 13)
