import random

def random_walk(n):
    '''return corrdinates after n block random walk'''
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return (x, y) #return as a tuple

for i in range(25):
    walk = random_walk(10)
    print(walk, 'Distance from home = ', abs(walk[0]) + abs(walk[1]))


number_of_walks = 20000
for walk_length in range(1, 31):
    no_transport = 0
    for i in range(number_of_walks):
        #print(i)
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_perc = float(no_transport / number_of_walks)
    print('walk size =', walk_length, ", % of no transport = ", 100 * no_transport_perc)

   