"""Set - A set is a collection of unique elements. It is an unordered data structure that does not allow duplicate values. Sets are commonly used to store and manipulate collections of items where uniqueness is important."""
# set - unordered, mutable, no duplicate elements

# s ={10,20,30,40}
# print(type(s))

"""********************v.v.v.v.v.important********************"""
# imp - you can only store hashable objects in a set. Hashable objects are those that have a hash value that does not change during their lifetime. This means that you can store immutable types like integers, floats, strings, and tuples in a set, but you cannot store mutable types like lists or dictionaries.
# example of hashable and non-hashable objects

# hashable
# s = {10, 20, 30, 40, (1, 2, 3), "hello"}
# print(s)

# non-hashable
# s = {10, 20, 30, 40, [1, 2, 3], "hello"} # TypeError: unhashable type: 'list'
# print(s)

"""********************v.v.v.v.v.important********************"""
# unordered nature
# s ={10,40,50,60,80}
# print(s)

# duplicates not allowed
# s = {10,10,20,20,30,30,40}
# print(s)


# traversing on the set
# s = {34,21,12,12,12,45,45,67,89}
# for i in s:
#     print(i)


"""**********************set Methods***************************"""
# s = {10,20,30,40,50}

# # s.add(11)

# print(s)


# difference()
# s1 = {10,20,30,40}
# s2 = {20,30,40,50,60}

# print(s2.difference(s1))
# print(s2 - s1)


# discard()
# s1 = {10,20,30,40}
# s2 = {20,30,40,50,60}

# s1.discard(40)
# print(s1)


# intersection()
# s1 = {10,20,30,40}
# s2 = {20,30,40,50,60}

# print(s1 & s2)

# pop()
# s1 = {1,2,3,4,5}
# s1.pop()

# print(s1)


# symmetric difference()
# s1 = {10,20,30,40}
# s2 = {20,30,40,50,60}

# print(s1 ^ s2)


# Union()
# a = {1,2,3}
# b = {3,4,5}

# print(a | b)


