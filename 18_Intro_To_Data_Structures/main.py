"""Intro to Data Structures - Lists, Tuples, Sets, and Dictionaries"""

# Lists -- ordered, mutable, allows duplicates
# Tuples -- ordered, immutable, allows duplicates
# Sets -- unordered, mutable, no duplicates
# Dictionaries -- unordered, mutable, no duplicates, key-value pairs

"""********** 1st - Lists ***********"""
# List - ordered, mutable, allows duplicates

# list = [10, 20, 30, 40, 50]

# print(list[0])  # List Indexing
# print(list[0:3]) # List Slicing


# mutablity
# a = [10, 20, 30, 45, 50]

# a[3] = 40
# print(a)


# ********reference copy**********
# a = [10, 20, 30, 40, 50]
# b = a

# b[0] = 100
# print(a)
# print(b)


# *********shallow copy***********
# a = [10, 20, 30, 40, 50]
# b = a.copy()

# b[0] = 100
# print(a)
# print(b)


# **********Deep Copy*************
# import copy

# a = [10, 20, 30, 40]
# b = copy.deepcopy(a)

# b[0] = 100
# print(a)
# print(b)


# 2nd level nested list
# a = [[10, 20], [30, 40]]
# b1 = a.copy()  # shallow copy
# b2 = copy.deepcopy(a)  # deep copy

# b1[0][0] = 999
# b2[1][0] = 888

# print("Original : ", a)  # [[999, 20], [30, 40]] <-- Shallow copy changes the original list
# print("Shallow : ", b1) # [[999, 20], [30, 40]] <-- Shallow copy changes the original list
# print("Deep : ", b2)   # [[10, 20], [888, 40]] <-- Deep copy does not change the original list


# traversing method 1
# a = [10, 20, 30, 40, 50]
# for i in a:
#     print(i)


# traversing method 2
# a = [10, 20, 30, 40, 50]
# for i in range(len(a)):
#     print(a[i])


# List methods
# a = [10, 20, 30, 40, 40, 40, 40]

# a.append(50)
# a.clear()
# print(a.count(40))
# print(a.index(40))
# a.insert(2, 20)
# a.pop()
# print(a)


"""*********************List Questions*******************************"""
# Q1
# list = [10, 20, 30, 40, 50]
# sum = 0

# for i in list:
#     sum = sum + i

# print(f"sum of your list numbers is - {sum}")
# print(f"average of your list numbers are - {sum/len(list)}")


# Q2 - find largest element
# list = [1, 24, 54, 3, 23, 43, 67, 89]
# max = list[0]
# index = 0

# for i in range(len(list)):
#     if list[i] > max:
#         max = list[i]
#         index = i

# print(max)


# Q3 - find 2nd greatest element
# list = [1, 24, 54, 3, 23, 43, 67, 89]
# max = list[0]
# max2 = list[0]
# index1 = 0
# index2 = 0

# for i in range(len(list)):
#     if list[i] > max:
#         max2 = max
#         max = list[i]
#         index2 = index1
#         index1 = i
#     elif list[i] > max2:
#         max2 = list[i]
#         index2 = i


# print(f"max {max} at index {index1} and max2 is {max2} at index {index2}")


# Q4 - check if list is Sorted
# a = [1, 2, 3, 4, 5, 6]

# for i in range(len(a) - 1):
#     if a[i] < a[i + 1]:
#         continue
#     else:
#         print("Your list is not sorted")
#         break

# else:
#     print("your list is sorted")


# Q5 - shift all elements one position to left, with the first element moving to the end
# a = [1, 2, 3, 4, 5, 6, 7]

# for i in range(len(a) - 1):
#     a[i], a[i + 1] = a[i + 1], a[i]

# print(a)


# Q6 - reverse the list
# a = [10, 20, 30, 40, 50, 60]
# b = []

# for i in range(len(a) - 1, -1, -1):
#     b.append(a[i])

# print(b)

# Q7- reverse a list without using extra space
# a = [10, 20, 30, 40, 50, 60]
# b = len(a) - 1

# for i in range(len(a) // 2):
#     a[i], a[b] = a[b], a[i]
#     b = b - 1

# print(a)


# Q7 - Searching - Linear Search
# a = [23, 43, 54, 45, 32, 1, 24, 5]
# search = 43

# for i in range(len(a)):
#     if a[i] == search:
#         print(f"Element found at index at {i}")
#         break
#     else:
#         print("sorry no such element exist")


# Q8 - binary search  **divide and quenqer method
# a = [12, 14, 16, 23, 32, 42, 54, 78, 90, 102]
# search = 32

# start = 0
# last = len(a) - 1
# mid = (start + last) // 2

# while start <= last:
#     if a[mid] == search:
#         print(f"element found at index -> {mid}")
#         break

#     elif a[mid] < search:
#         start = mid + 1
#         mid = (start + last) // 2

#     elif a[mid] > search:
#         last = mid - 1
#         mid = (start + last) // 2

# else:
#     print("sorry no such element exist")


# Q8 - bubble sort
# a = [34, 54, 3, 4, 2, 3, 5, 5, 65, 67, 87, 3, 4, 5, 22, 675, 7000, 65, 5]

# for j in range(len(a) - 1):
#     for i in range(len(a) - 1 - j):
#         if a[i] > a[i + 1]:
#             a[i], a[i + 1] = a[i + 1], a[i]

# print(a)


# Q9 - selection sort
# a = [34, 54, 3, 4, 2, 3, 5, 5, 65, 67, 87, 3, 4, 5, 22, 675, 7000, 65, 5]

# for i in range(len(a) - 1):
#     j = i + 1
#     min = i
#     for k in range(j, len(a)):
#         if a[k] < a[min]:
#             min = k

#     a[i], a[min] = a[min], a[i]

# print(a)
