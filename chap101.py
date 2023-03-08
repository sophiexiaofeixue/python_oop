# aggregation vs composition

# aggregation
# class B has an instance of class A but they can both exist independently

class Die:

    def __init__(self, value):
        self.value = value

class Player:
    
    def __init__(self, die):
        self.die = die

my_die = Die(5)
my_player = Player(my_die)

# composition
# a composed object cannot exist without the object that contains it
class Die:

    def __init__(self, value):
        self.value = value


class Player:

    def __init__(self):
        self.die = Die(5)
        # this particular Die instance cannot exist withought the Player instance that contains it

my_player = Player()