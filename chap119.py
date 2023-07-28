# 119 - introduction to is
# obj1 is obj2
# if these 2 objects are refering to the same object
# boolean
# identity comparison

# is and is not
# id() function
# == checks the values not the object identity
# the two objects may be the same value but in different memory location

a = [1, 6, 2, 6]
b = [1, 6, 2, 6]

print(a is b)
print(a == b)

print(id(a))
print(id(b))

class Dog:

    def __init__(self, age):
        self.age = age

a = Dog(5)
b = Dog(5)
print(a == b)
# this will return false
# objects created from user-defined classes have to meet 2 conditions
# for the expression obj1 == obj2 to be True
# 1) they have to refer to the same object (x is y has to evaluate to True)
# 2) the expression hash(x) == hash(y) has to be True

# 2)
print(hash(a))
print(hash(b))