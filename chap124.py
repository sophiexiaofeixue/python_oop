# chap124
# objects can be passed by value or reference
# in python objects are passed by reference

my_list = [6, 2, 8, 2]

def print_data(seq):
    print("inside the function:", id(seq))
    for elem in seq:
        print(elem)

print("outside the function:", id(my_list))
print_data(my_list)
# seq is an object, like list
# it is passed by reference

def multiply_by_two(seq):
    print("inside the function:", id(my_list))
    for i in range(len(seq)):
        seq[i] *= 2

# modify the sequence
print("outside the function:", id(my_list))
multiply_by_two(my_list)
print(my_list)
# we modified the original object, we did not make a copy of this object

class Sale:

    def __init__(self, amount):
        self.amount = amount

def find_total(sales):
    total = 0

    for sale in sales:
        print("new sale...")
        print(sale.amount)
        total += sale.amount
    return total

jan_sales = [Sale(400), Sale(345), Sale(45)]

print(find_total(jan_sales))