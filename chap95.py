# method chaining
# add many things to a class
class Pizza:

    def __init__(self):
        self.toppings = []
    
    def add_topping(self, new_topping):
        self.toppings.append(new_topping.lower())
        return self #this is the method chaining line
        # it returns self, so you can use it to call another method
        # in the same line

    def display_toppings(self):
        print('This pizza has:')
        for topping in self.toppings:
            print(topping.capitalize())

pizza = Pizza()
pizza.add_topping('mushrooms') \
     .add_topping('olives') \
     .add_topping('chicken') \
     .display_toppings()

# in the past we have to write this line be line.
# now it can ge written in one line.
# method chaining made the code more concise and readable