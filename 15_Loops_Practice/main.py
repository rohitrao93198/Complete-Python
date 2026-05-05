# Q1
# a = 145
# a = int(input("ENter any number: "))

# while a > 0:
#     print(a % 10)
#     a = a // 10

# Q2
# a = int(input("Enter any number: "))
# sum = 0

# while a > 0:
#     sum = sum + a % 10
#     a = a // 10

# print(f"Your sum is: ",sum)


# Q3 - Reverse a number
# a = int(input("Enter any number: "))
# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print(rev)


# Q4 - Check the no is palindrom or not
# a = int(input("Enter any Number: "))
# copy = a
# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# if rev == copy:
#     print("Yes your number is pallindrome")
# else:
#     print("Sorry your number is not pallindrome")


# Q5 - Check the number is automorphic number or not
a = int(input("Enter any number : "))
dup = a

square = a ** 2 # 625
count = 0

while a > 0:
    count = count + 1
    a = a// 10

extract = square % (10**count)

if extract == dup:
    print("your number is automorphic")
else:
    print("Sorry your number is not automorphic")







