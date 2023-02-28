class Backpack:
    def __init__(self):
        self._items = []
    
    @property
    def items(self):
        print('calling the getter')
        return self._items
    
    @items.setter
    def items(self, new_items):
        print('calling the setter')
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print('please enter a valid list')

my_backpack = Backpack()
print(my_backpack.items)
my_backpack.items = ['water bottle', 'sleeping bag']
print(my_backpack.items)

my_backpack.items = 'hello world'
print(my_backpack.items)