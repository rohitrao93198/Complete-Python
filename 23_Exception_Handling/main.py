"""Exception Handling --> eksa matlab hota hai ki jab hum apne code mein koi aisi cheez karte hain jo galat ho sakti hai, toh uss galti ko handle karna. Jaise ki agar hum kisi file ko read karna chahte hain jo exist nahi karti, toh wo error dega. Exception handling se hum uss error ko gracefully handle kar sakte hain, taki program crash na ho aur user ko ek accha message mile ki kya galti hui hai."""

# Example of exception handling in Python
# a = int(input("Provide 1st number : "))
# b = int(input("Provide 2nd number : "))

# try:
#     print(a/b)
# except Exception as err:
#     print("sorry an error occured")

# print(a+b)


# try except else
# a = int(input("Provide 1st number : "))
# b = int(input("Provide 2nd number : "))

# try:
#     print(a/b)
# except Exception as err:
#     print("sorry an error occured")

# else:
#     print("there was no error")

# print(a+b)



# try except else and finally
# a = int(input("Provide 1st number : "))
# b = int(input("Provide 2nd number : "))

# try:
#     print(a/b)
# except Exception as err:
#     print("sorry an error occured")

# else:
#     print("there was no error")

# finally:
#     print("i will execute no matter what !!")

# print(a+b)



# raise
# try:
#     age = int(input("Enter your age : "))
#     if age < 18:
#         raise Exception("You must be 18+")
#     print("Access granted")
# except Exception as err:
#     print("error : ", err)