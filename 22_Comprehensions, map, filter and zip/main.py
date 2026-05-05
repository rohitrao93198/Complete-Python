"""lambda expression - anonymous function, a function that is defined without a name.It can take any number of arguments, but can only have one expression. The expression is evaluated and returned when the function is called.
Syntax: lambda arguments: expression"""

# Example 1: A simple lambda function that adds two numbers
# add = lambda x, y: x + y
# print(add(5, 3))  # Output: 8


"""map ---> a built-in function that applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator). The syntax is: map(function, iterable)""" 

# a = [1, 2, 3, 4, 5]
# square = map(lambda x: x**2, a) 
# print(list(square))


"""filter ---> in easy language, ye filter function ek aise function ko leta hai jo true ya false return karta hai (jaise ki lambda function) aur ek iterable (jaise ki list). Ye function iterable ke har element par apply hota hai, aur sirf un elements ko return karta hai jinke liye function true return karta hai. Jab aap is filter object ko list me convert karte hain, to aapko ek list milti hai jisme sirf wo elements hote hain jo condition ko satisfy karte hain."""

# a = [1,2,3,4,5,6,7,7,8,9,10]
# even = filter(lambda x: x %2 == 0, a)
# print(list(even))


"""zip ---> in easy language, ye zip function do aise kaam karta hai ki agar aapke paas do ya usse zyada lists hain, to ye unke corresponding elements ko ek saath jod kar ek tuple bana deta hai. Aur ye tuples ka ek iterator return karta hai. Jab aap is iterator ko list me convert karte hain, to aapko ek list of tuples milti hai, jisme har tuple me corresponding elements hote hain."""

# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# zipped = zip(a, b)
# print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


"""List comprehension ---> ek concise way hai list banane ka. Iska syntax hai: [expression for item in iterable if condition]. Yahan, expression wo value hai jo aap list me rakhna chahte hain, item wo variable hai jo iterable ke har element ko represent karta hai, aur condition ek optional part hai jo specify karta hai ki kaunse elements ko include karna hai."""

# a = [1,2,3,4,5,6,7,8,9,10]

# l = [i for i in a if i % 2 == 0]

# print(l)


# set compherension
# a = [1,2,3,4,5,6,7,8,9,10]

# l = {i for i in a if i % 2 == 0}

# print(l)


# dictionary compherension
# a = [1,2,3,4,5,6,7,8,9,10]

# l = {i:i**2 for i in a if i%2 == 0}

# print(l)


"""Generator comprehension ---> ek concise way hai generator banane ka. Iska syntax hai: (expression for item in iterable if condition). Yahan, expression wo value hai jo aap generator me rakhna chahte hain, item wo variable hai jo iterable ke har element ko represent karta hai, aur condition ek optional part hai jo specify karta hai ki kaunse elements ko include karna hai."""

# a = [1,2,3,4,5,6,7,8,9,10]
# l = (i for i in a if i % 2 == 0)
# print(l)  # Output: <generator object <genexpr> at 0x7f8b8c8c8c8c>
# print(list(l))  # Output: [2, 4, 6, 8, 10]


# def my_generator():
#     for i in range(5):
#         yield i

# # print(my_generator())
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(list(gen)) 


# sequence = (x**2 for x in range(5))

# print(next(sequence))
# print(next(sequence))
# print(next(sequence))
# print(next(sequence))


"""Decorator --> ek function hai jo doosre function ko modify karta hai bina uske structure ko change kiye. Iska syntax hai: @decorator_name. Jab aap kisi function ke upar @decorator_name likhte hain, to wo function decorator_name ke andar pass ho jata hai, aur decorator_name us function ko modify karke return karta hai."""

# def my_decorator(func):
#     def wrapper():
#         print("hello i will print before")
#         func()
#         print("hello i will print after")
#     return wrapper    


# @my_decorator
# def say_hello():
#     print("hello")

# say_hello()


def decorate(func):
    def wrapper(a,b):
        print("Your 2 numbers addition is : ")
        func(a,b)
        print("Thank you for using us")
    return wrapper

@decorate
def addition(a,b):
    print(a+b)

addition(1,5)