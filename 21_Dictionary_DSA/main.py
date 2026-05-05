"""Dictionary - A collection of key-value pairs where each key is unique.
It is implemented as a hash table, which allows for efficient insertion, deletion, and retrieval of values based on their keys. Dictionaries are commonly used in programming for tasks such as data storage, lookup, and mapping."""
# dictionary - mutable, ordered, not duplicate allowed and key based access
# keys must be unique and immutable (e.g., strings, numbers, tuples)

# d = {1:10}
# print(type(d))

# d = {10:100, 20:200, 30:300}
# print(d[10])

# d = {"hello": 100, "rohit": 200}
# print(d["hello"]) # access the values
# d["rohit"] = 5000 # change the value
# print(d)


# dictionary constructor()
# d = dict(name = "Rohit", age = 24, gender = "Male")
# print(d)


# Dictionary Traversing
# a = {10: 100, 20:200, 30:300, 40:400}

# 1st way
# for i in a:
#     print(a[i]) 

# for i in a.values():
#     print(i)


"""************Dictionary Methods**************************"""
# a = {10: 100, 20:200, 30:300, 40:400}
# b = {50:500, 60:600, 70:700}

# print(a.get(20))
# print(a.items())
# print(a.keys())

# a.update(b)
# print(a)



"""*********************** - Questions - ***************************"""
# Q1 - print unique elements in array
# a = [1,1,1,2,2,2,2,2,2,2,3,4,3,3,3,4,4,4,5,5,6,6,6,6]
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d.keys())


# Q2 - count frequency of array elements
# a = [1,1,1,2,2,2,2,2,2,2,3,4,3,3,3,4,4,4,5,5,6,6,6,6]

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d)


# Q3 - check if Two Strings have same frequency map
# s1 = "aabbcc"
# s2 = "baccab"

# if len(s1) == len(s2):
#     d={}
#     for i in s1:
#         if i in d.keys():
#             d[i] = d[i] + 1
#         else:
#             d[i] = 1

#     for i in s2:
#         if i in d.keys():
#             d[i] = d[i] - 1
#         else:
#             print("an extra element was fond")

#     for i in d:
#         if d[i] != 0:
#             print("sorry your elements are not same")
#             break
#         else:
#             print("your strings are same")

# else:
#     print("not same")


# Q4 - detect and print elements that appear more than once in the array
# a = [1,1,2,2,3,4,54,5,4,3,2,4,5,6,7]
# d={}

# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1 

# for i in d:
#     if d[i] > 1:
#         print(i)


# Q5 - return all unique elements that appear in both arrays
a = [1,22,1,2,2]
b = [2,3,2]

j = []
d = {}

for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for i in d.keys():
    if i in b:
        j.append(i)
    
print(j)










