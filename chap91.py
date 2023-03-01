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
            return 0
        
    def has_item(self, item):
        return item in self._items
    
    def show_items(self, sorted_list = False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)
    
my_backpack = Backpack()
my_backpack.add_item('water bottle')
my_backpack.add_item('sleeping bag')
my_backpack.add_item('candy')

print('not sorted:')
my_backpack.show_items()

print('sorted:')
my_backpack.show_items(True)