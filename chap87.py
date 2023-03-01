class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print('please provide a valid item')
    
    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            print('this item is not in the backpack')
            return 0
    
    def has_item(self, item):
        return item in self._items
    
my_backpack = Backpack()
print(my_backpack.items)

my_backpack.add_item('water bottle')
print(my_backpack.items)

my_backpack.add_item('sleeping bag')
print(my_backpack.items)

my_backpack.has_item('water bottle')
has_water = my_backpack.has_item('water bottle')
print(has_water)

my_backpack.remove_item('sleeping bag')
print(my_backpack.items)

my_backpack.remove_item('candy bar')
