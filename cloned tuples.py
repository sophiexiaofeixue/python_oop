# cloned tuples
# have hte same id
# why?

my_tuple = (1, 2, 3, 4)
cloned_tuple = my_tuple[:] # clone the tuple
print(id(my_tuple))
print(id(cloned_tuple))
# the 2 id are the same

# it will not happen if we cloned the list
my_list = [1, 2, 3, 4]
cloned_list = my_list[:]
print(id(my_list))
print(id(cloned_list))

# why?
# tuples are immutable in python.
# you cannot create a new tuple in memory by cloning

# the purpose of cloning is to create a copy of the object that you can modify without mutating the original
# in practice, we cannot really create a clone of a tuple
# we can only assign a reference to the original tuple to another variable

# creating alias can introduct bugs because you could modify an object without realizing that the change
# will affect the object being referenced by the other alias

# the keys of a dictionary must be immutable objects like tuples and strings