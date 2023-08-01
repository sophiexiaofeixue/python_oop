# mutable and immutable
# advantage and disadvantage

# mutable objects
# 1) memory efficiency
# 2) real world objects
# 3) introduce bugs

def add_absolute_values(seq):
    for i in range(len(seq)):
        seq[i] = abs(seq[i])
    return sum(seq)

values = [-5, -6, -7, -8]
print("values before:", values)
# however we changed the list to a new list
# this is against our intention
print(add_absolute_values(values))
print("values after:", values)
# prune to unexpected changes

# potential risks of aliasing
# 1) mutating object, mutate an object unintentionally through an alias

a = [1, 2, 3, 4]
b = a
b[0] = 15
print(b)
print(a)

# advantages of immutable objects
# 1) prevent bugs
# 2) easier to understand, we know the exact value
# 3) less efficient in terms of memory usage

a = (1, 2, 3, 4)
print(id(a))
# have to add an element in
# but it is immutable
a = a[:2] + (7, ) + a[2:]
print(a)
print(id(a))
# this is a new object
# the old object is no longer accessible after we updated the variable
# the variable a is only for the new a we created

