import random

def random_walk_2(n):
    '''return coordinates after n block random walk'''
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx #difference in x
        y += dy #difference in y
    return (x, y)

for i in range(25):
    walk = random_walk_2(10)
    print(walk, 'Distance from home = ', abs(walk[0]) + abs(walk[1]))