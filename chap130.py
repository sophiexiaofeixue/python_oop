#chap130

# alias in programming
# different name, same object
# 2 or more references to the same memory address in the program

a = [1, 2, 3, 4]
b = a

print(id(a))
print(id(b))
# if id is the same, then we have 2 alias referencing the same object

print(a is b)

c = b
d = c
print(a is b is c is d)


class Circle:

    def __init__(self, radius):
        self.radius = radius

my_circle = Circle(4)
your_circle = my_circle

print(my_circle is your_circle)
# risks
# you can modify your_circle thinking it will not affect my_circle

print("before")
print(my_circle.radius)
print(your_circle.radius)

your_circle.radius = 18
print("after")
print(my_circle.radius)
print(your_circle.radius)

class Backpack:

    def __init__(self):
        self._items = []
    
    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        if item in self._items:
           self._items.remove(item)
        else:
            print("this item is not in the backpack") 


my_backpack = Backpack()
your_backpack = my_backpack
her_backpack = your_backpack
print(my_backpack is your_backpack is her_backpack)

my_backpack.add_item("water bottle")
my_backpack.add_item("candy")

print(my_backpack.items)
print(your_backpack.items)
print(her_backpack.items)