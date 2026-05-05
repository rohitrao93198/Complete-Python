"""Conditional statements are used to perform different actions based on different conditions. In Python, we use if, elif, and else statements to implement conditional logic."""

# Example 1: Basic if statement
age = 18
if age >= 18:
    print("You are an adult.")


# Example 2: if-else statement
age = 16
if age >= 18:
    print("You are an adult.")
else:   
    print("You are a minor.")


# Example 3: if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Example 4: Nested if statements
num = 10
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")

# Example 5: Using logical operators in if statements
age = 25
if age >= 18 and age < 65:
    print("You are of working age.")

# Example 6: Using the ternary operator for conditional expressions
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)


#excercise
# a,b = input("Enter two numbers separated by space: ").split()
# a = int(a)
# b = int(b)

# if a > b:
#     print(f"{a} is greater than {b}.")
# elif a < b:
#     print(f"{b} is greater than {a}.")
# else:    print("Both numbers are equal.")


#2
# gender = input("Enter your gender: ").lower()
# if gender == "male":
#     print("You are a man")
# else:
#     print("You are a woman")


#3
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#    print(f"{number} is odd.")


#4
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# if age >= 18:
#     print(f"hello {name} you are a valid voter")
# else:
#     print(f"sorry {name} you are not eligible for vote")

#5
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("it is a leap year")
        else: 
            print("it is a common year")
    else: 
        print("it is a leap year")
else:
    print("no it is a common year")

# 5 check leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")




