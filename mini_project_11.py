# mini project 11
# alias, mutation, clone

# Explain the relationship between aliasing, mutation, and cloning. Briefly explain each concept.

# alias: create a another variable to reference to the same object in the memory using a different name
# we can use alias on mutable and immutable variables
# we can modify mutable objects
# we cannot modify immutable objects
# cloning is to create a same object, but store the cloned copy
# in a different memory location, and it is independent from the original object

# With your knowledge of aliasing, mutation, and cloning,
# modify the functions in the following program so that the original list is not mutated.


# a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
# b = a
# c = b
# b = c
 
# def remove_elem(data, target):
#     for item in data:
#         if item == target:
#             data.remove(target)
#     return data
 
# def get_product(data):
#     total = 1
#     for i in range(len(data)):
#         print(i)
#         total *= data.copy().pop()
#     return total
 
# print(remove_elem(c, 3))
# print(get_product(b))
# print(a)

# solution
a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a[:]
c = a[:]
 
def remove_elem(data, target):
    for item in data:
        if item == target:
            data.remove(target)
    return data
 
def get_product(data):
    total = 1
    for i in range(len(data)):
        total *= data.pop()
    return total
 
print(remove_elem(c, 3))
print(get_product(b))
print(a)