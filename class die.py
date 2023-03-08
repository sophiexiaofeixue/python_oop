import random

class Die:

    # value should be none by default before rolling
    def __init__(self, value = None):
        self._value = value
    # def __init__(self):
          #self._value = None

    @property
    def value(self):
        return self._value
    # we have getter
    # we do not have setter
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value

# test
my_die = Die()
print(my_die.value)

my_die.roll()
print(my_die.value)

new_value = my_die.roll()
print(new_value)