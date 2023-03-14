# built in methods for list
# extend, append, insert, count, index, sort, pop, remove
a = [1, 5, 6, 2, 8]
print(a)
a.extend([7, 2])
print(a)
a.append(8)
print(a)
a.insert(1, 3)
print(a)
print(a.count(2))

print(a.index(5))
print(a.index(3))
a.sort()
print(a)
print(a.pop())
print(a)
a.remove(2)
print(a)

# tuple
# count, index
b = (1, 6, 2, 8)
print(b.count(6))
print(b.index(2))

# string
# capitalize, casefold, count, isdigit, islower, isspace, replace, strip

# dictionary
# get, keys, values, items, popitem