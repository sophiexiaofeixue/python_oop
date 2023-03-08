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


class Player:

    def __init__(self, die, is_computer = False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10
    
    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1
    
    def roll_die(self):
        return self._die.roll()
        # access the player attribute die and die method roll
        # i need to review the aggregation

# test
die_1 = Die()
# you need to create the die instance for the Player instance
my_player = Player(die_1, is_computer = False)
print(my_player)
print(my_player.die) # we have die instance of that player
print(my_player.is_computer)
print(my_player.counter)
my_player.increment_counter()
print(my_player.counter)
my_player.decrement_counter()
print(my_player.counter)

print(die_1.value)
my_player.roll_die()
print(die_1.value)
print(my_player.die.value)


