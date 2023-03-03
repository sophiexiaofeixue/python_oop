# call a method from another method
class Backpack:

    def __init__(self):
        self._items = []
    
    @property
    def items(self):
        return self._items
    # how to add multiple items at once
    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)

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
            return 0
    
    def has_item(self, item):
        return item in self._items
    
    def show_items(self, sorted_list = False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)

my_backpack = Backpack()
print(my_backpack.items)

my_backpack.add_multiple_items(['water bollte', 'candy'])
print(my_backpack.items)

my_backpack.add_item(['sleeping bag', 'flash light']) #this will not work