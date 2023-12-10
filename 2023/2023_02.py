from utils import *

inp = get_input(2023,2)

# Process the input
# Processed is just the list of games with all the pulls
# Where you keep track of blue,green,red pulls
processed = dd(list)
for game in inp:
    s = game.split(':')
    num = int(s[0].split(' ')[1])
    pulls = s[1].split(';')
    for pull in pulls:
        
        # cts = [b, g, r]
        cts =   [0, 0, 0]
        cubes = pull.split(',')
        for cube in cubes:
            [emp, ct, col] = cube.split(' ')
            ct = int(ct)
            
            if col=='blue':
                cts[0]+=ct
            if col=='green':
                cts[1]+=ct
            if col=='red':
                cts[2]+=ct
        processed[num].append(cts)
        
# Function to check if a given processed game is viable        
def checkViable(game, bMax, gMax, rMax):
    for pull in game:
        if (pull[0]>bMax)|(pull[1]>gMax)|(pull[2]>rMax):
            return(0)
    return(1)        


# Function to get the power of a game.
def getPower(game):
    best = [0, 0, 0]
    for pull in game:
        best = [max(best[0],pull[0]), max(best[1],pull[1]), max(best[2],pull[2])]
    return math.prod(best)


# Do the calculations
A = 0
B = 0
for n in processed:
    # Part A
    if checkViable(processed[n],14,13,12):
        A+=n
    
    # Part B
    B+=getPower(processed[n])


print('Part A Solution:', A)
print('Part B Solution:', B)
