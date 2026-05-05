# Q1
# nums = int(input("Enter a number: "))
# for i in range(nums):
#     print(f"Hello World {i}")


# Q2
# nums = int(input("Enter a number: "))
# for i in range(1,nums+1):
#     print(i)


# Q3
# nums = int(input("Enter a number: "))
# for i in range(nums,0, -1):
#     print(i)


# Q4
# nums = int(input("Enter a number: "))
# sum = 0
# for i in range(1, nums + 1):
#     sum = sum + i

# print("Sum = ", sum)

# Q5 Factorial of a number
# nums = int(input("Enter a number: "))
# fact = 1
# for i in range(1, nums + 1):
#     fact = fact * i

# print("Factorial = ", fact)

# Q10
# nums = int(input("Enter a number: "))
# even_sum = 0
# odd_sum = 0

# for i in range(1, nums + 1):
#     if i % 2 == 0:
#         even_sum = even_sum + i
#     else:
#         odd_sum = odd_sum + i

# print("Even sum = ", even_sum)
# print("Odd sum = ", odd_sum)


# Q11 find factors of a number
# nums = int(input("Enter a number: "))
# factors = 0
# for i in range(1, nums + 1):
#     if nums % i == 0:
#         print(i)


# Q12 sum of all factors
# nums = int(input("Enter a number: "))
# factors = 0
# for i in range(1, nums + 1):
#     if nums % i == 0:
#         factors = factors + i

# print(factors)


# Q13
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# power = num1

# for i in range(num2 - 1):
#     power = power * num1

# print("After power your answer is - ", power)


# Q14
# num = int(input("Enter a number: "))
# count = 0
# for i in range(1, num+1):
#     if num % i == 0:
#         count = count + 1

# if count == 1:
#     print("your number is a unity number")
# elif count == 2:
#     print("your numbner is prime")
# else:
#     print("your no is composite")


# 2nd way
# num = int(input("Enter a number: "))
# for i in range(2, num):
#     if num % i ==0:
#       print("Sorry your number is composite")
#       break

# else:
#     print("Your no is prime no")


for i in range(3):
    for j in range(2):
        print(i, j)


















