#methods in python
#a method is a function associated to an object of the class
#or to the class itself
#the methods defined in a class determine the behavior of the objects
#created from that class and how they interact with their state

#3 types of methods
#instance, class, static

#instance methods. methods that belong to a specific object
#they have access to hte state of the object that calls them
#calling a method is very similar to calling a function
#a method is a function that belongs to an object

#method names usually include verbs since they represent actions
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def find_diameter(self): #instance method
        print(f"Diameter: {self.radius * 2}")

    def get_diameter(self):
        return self.radius * 2

my_circle = Circle(5)

