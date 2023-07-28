# chap122
a = 5
b = 5
print(a is b) # True

# small integers
# [-5, 256]

a = 257
b = 257
print(a is b) # true
# vscode is optimizing it
# will not work if using a different IDE

# strings
# via string interning
a = "h"
b = "h"
print(a is b) # true
# strings are immutable, cannot be changed, no need to create the same object again and again
# string interning = the process of keeping only 1 distinct copy of the string in memory
print(id(a))
print(id(b))

# different behavior shell vs script