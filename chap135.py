#chap135

# built-in methods can mutate objects
a = [6, 2, 7, 1]
a.sort()
print(a)

a = [6, 2, 7, 1]
result = sorted(a)
print("the sorted list is", result)
print(a)

class WaitingList:

    def __init__(self, clients=[]): # the default argument is an empty list
        self.clients = clients
        print("list id:", id(self.clients))
        # self.clients references the same list in the 
    
    def add_client(self, client):
        self.clients.append(client)

# create instances
waiting_list_1 = WaitingList()
waiting_list_2 = WaitingList()

waiting_list_1.add_client("Jake")
#but both list are modified
print(waiting_list_1.clients)
print(waiting_list_2.clients)

# solution to the above problem
# avoid using the list directly as a default argument, and use something else instead
class WaitingList:

    def __init__(self, clients = None):
        if clients == None:
            self.clients = []
        else:
            self.clients = clients
    
    def add_client(self, client):
        self.clients.append(client)

waiting_list_1 = WaitingList()
waiting_list_2 = WaitingList()
waiting_list_1.add_client("Jake")
print(waiting_list_1.clients)
print(waiting_list_2.clients)

# important tip
# immutable does not mean that its element are immutable
# immutable objects contain mutable objects and
# these mutable objects can be modified even if the container cannot be modified
a = ([1, 2, 3], "abc", 56)
a[0] = 12 # will get an error

a[0][1] = 4 # will not get an error
# choose an immutable container object, ie a tuple, does not protect the elements inside of tuple
# from being changed if they are mutable, ie a list