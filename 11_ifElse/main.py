#1
# a,b = input("Enter two numbers: ").split()
# a = int(a)
# b = int(b)
# if a>b:
#     print(f"{a} is greater than {b}")
# elif b>a:
#     print(f"{b} is greater than {a}")
# else:
#     print(f"Both {a} and {b} are equal")

# 2
# gender = input("Enter your gender: ").lower()
# if gender == "m":
#     print("Hello Sir")
# elif gender == "f":
#     print("Hello mam")
# else:
#     print("Wrong input")

# 3
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("it is a even number")
# else:
#     print("it is a odd number")

# 4
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# if age >=18:
#     print(f"Hello {name} you are eligible for vote")
# else:
#     print(f"sorry {name} your are not eligible")

# 5
# number = int(input("Enter a number 1-7: "))
# if number == 1:
#     print("Monday")
# elif number == 2:
#     print("Tuesday")
# elif number == 3:
#     print("Wednesday")
# elif number == 4:
#     print("Thursday")
# elif number == 5:
#     print("Friday")
# elif number == 6:
#     print("Saturday")
# else:
#     print("Wow it's sunday")


# 6
# a, b, c = input("Enter three numbers: ").split()
# a = int(a)
# b = int(b)
# c = int(c)
# if a > b and a >c:
#     print(f"{a} is the greatest number")
# elif b >a and b > c:
#     print(f"{b} is the greatest number")
# else:
#     print(f"{c} is the greatest number")

# 7
# a,b ,c = input("ENter three numbers: ").split()
# a = int(a)
# b = int(b)
# c = int(c)
# if a == b and b == c:
#     print("all the numbers are equal")
# elif a == b or b == c or c == a:
#     print("any two numbers are equal")
# elif a> b and a > c:
#     print(f"{a} is the greatest number")
# elif b > a and b > c:
#     print(f"{b} is the greatest number")
# else:
#     print(f"{c} is the greatest number")


# 8
# bill = int(input("please tell your total amount: "))
# if bill >=1000 and bill <=4999:
#     print(f"you got a discount of 10% : your final amount is {(bill * 90) / 100}")
# elif bill >=5000:
#     print(f"you got a discount of 20% : your final amount is {(bill * 80) / 100}")
# else:
#     print("Sorry no discount for you")

# 9
# char = input("Enter a single character: ").lower()
# if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#     print("its a vowel")
# else:
#     print("its a consonent")

# 10
char = input("Enter a single character: ")
if char in "aeiouAEIOU":
    print("its a vowel")
else:
    print("its a consonent")





