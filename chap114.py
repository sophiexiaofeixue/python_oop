# objects in memory
# in python everything is an object
print(object)
# object is the base class
print(isinstance(5, object))
print(isinstance([1, 5, 2, 6], object))
print(isinstance((1, 5, 2, 6), object))
print(isinstance('hello, world', object))
print(isinstance({'a':5, 'b':6}, object))
print(isinstance(False, object))

def f(x):
    return x * 2

print(isinstance(f, object))

class Movie:

    def __init__(self, title):
        self.title = title


print(isinstance(Movie, object))

# everything is an object
# integer, float, boolean, function, list, tuple, dictionary, string, exception

# an object is stored in memory with an ID
# ID is the memory location in computer
# programs keep track of how many references to the object exists
# a reference is a name that refers to the location in memory of an object
# reference includes variables, attribute, items
# variables in python store references to objects in memory
# when there are no references to the object in the program, the object is deleted from memory
# garbage collection = when an object is deleted from memory by python automatically