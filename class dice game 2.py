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


class DiceGame:

    def __init__(self, human, computer):
        self._human = human
        self._computer = computer
    
    def play(self):
        print('============================================')
        print('welcome to roll the dice 🎲')
        print('============================================')
        while True:
            # this is an infinite loop
            # will stop at BREAK
            self.play_round()
            # to do: implement game over
    
    def play_round(self):
        # welcome player to this round
        self.print_round_welcome()

        # roll the dice
        human_value = self._human.roll_die()
        computer_value = self._computer.roll_die()

        # show the values - can be converted to a method
        self.show_dice(human_value, computer_value)

        # determine who won
        if human_value > computer_value:
            print('you won this round')
            self.update_counters(winner = self._human, 
                                 loser = self._computer)

        elif human_value < computer_value:
            print('computer won this round')
            self.update_counters(winner = self._computer,
                                 loser = self._human)
            
        else:
            print('this is a tie')
        
        # show counters
        self.show_counters()
    
    def print_round_welcome(self):
        print('---new round---')
        input('press any key to roll the dice')
    
    def show_dice(self, human_value, computer_value):
        print(f"your die: {human_value}")
        print(f"computer die: {computer_value}")
    
    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()
    
    def show_counters(self):
        print(f'your counter is: {self._human.counter}')
        print(f'computer counter is: {self._computer.counter}')



# create die instance for chaining
human_die = Die()
computer_die = Die()
# create player instance for chaining
player_1 = Player(human_die, is_computer=False)
player_2 = Player(computer_die, is_computer = True)
game = DiceGame(player_1, player_2)
# start the game
game.play()