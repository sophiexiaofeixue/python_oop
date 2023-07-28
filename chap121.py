# chap121
a = [5, 2, 1, 8, 3]
b = [6, 2, 8, 9, 3]

print(a is b)

b = a
print(a is b) # referce to the same object

c = ("a", "b", "c")
d = ("e", "f")

print(c is d)
print(d is c) # return false

e = "hello world"
f = "hello world"

print(e is f)
print(f is e) # return true
# why
# next lesson