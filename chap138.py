#chap138
#cloning

# create an exact copy of the object that is completely independent from the original object
# it is like the opposite of aliaing
# it is completely independent
# all the same attributes, methods, and etc
a = [6, 2, 6, 2]
b = a[:] # clone the list
# get all the elements from list a
b[0] = 15
print(id(a))
print(id(b))
print(a)
print(b)

def remove_even_values(dictionary):
    for key, value in dictionary.copy().items(): # note: copy() here
        if value % 2 == 0:
            del dictionary[key]

my_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
remove_even_values(my_dictionary)
print(my_dictionary)

# shallow vs deep copy of an object

# shallow copy
# make a new object in memory, a new reference, but the content of the object will still point to the same objects
a = ([0, 6, 2], "tuple", 56)
b = a[:]
b[0][0] = -1 # we are modifying the list in memory
print(a)
print(b)
# we have to be very careful about this

# another bug example
a = {"Nora":["055-452-322", "washington ave"], "Gino":["006-545", "5th avenue"]}
b = a.copy()
print(a)
print(b)
b["Nora"][0] = "56"
print(b)
print(a)
# it is not foolproof

import copy
a = ([5, 2, 6, 2], "welcome", 67)
b = copy.copy(a)
print(b)
b[0][0] = -1
print(b)
print(a)

# deep copy
# with deep copy, in addition to creating a copy of the container object, 
# you also create a copy of the elements contained in the object
# in order to deep copy, you need to use copy()

import copy
a = ([5, 2, 6, 2], "Welcome")
b = copy.deepcopy(a)
b[0][0] = -1
 
# Changing the list in b did not affect the list in a
print(a)
print(b)