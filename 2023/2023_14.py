from utils import *

inp = get_input(2023,14)

g = grid2dict(inp)
h = len(inp)
w = len(inp[0])

# The dumbest approach.
# Lots of cool ideas for how to actually do the movement out there
# also could just rotate the grid and have a single "north" movement
# but why be clever when you can do tedious casework and copy/paste code?
def cycle(grid):
    g = dc(grid)     
    # North
    for i in range(h):
        for j in range(w):
            if g[(i,j)]=='O':
                k=1
                while i-k>=0 and g[(i-k,j)]=='.':
                    k+=1
                g[(i,j)]='.'
                g[(i-k+1,j)]='O'
    # West
    for j in range(w):
        for i in range(h):
            if g[(i,j)]=='O':
                k=1
                while j-k>=0 and g[(i,j-k)]=='.':
                    k+=1
                g[(i,j)]='.'
                g[(i,j-k+1)]='O'
    # South
    for i in range(h-1,-1,-1):
        for j in range(w):
            if g[(i,j)]=='O':
                k=1
                while i+k<h and g[(i+k,j)]=='.':
                    k+=1
                g[(i,j)]='.'
                g[(i+k-1,j)]='O'
    # East
    for j in range(w-1,-1,-1):
        for i in range(h):
            if g[(i,j)]=='O':
                k=1
                while j+k<w and g[(i,j+k)]=='.':
                    k+=1
                g[(i,j)]='.'
                g[(i,j+k-1)]='O'
    return(g)

def load(g):
    total = 0
    for i in range(h):
        for j in range(w):
            if g[(i,j)]=='O':
                total+=(100-i)
    return(total)

# Calculation for A
north = dc(g)
for i in range(h):
    for j in range(w):
        if north[(i,j)]=='O':
            k=1
            while i-k>=0 and north[(i-k,j)]=='.':
                k+=1
            north[(i,j)]='.'
            north[(i-k+1,j)]='O'

# B
# Need to figure out the cycle length
# and then figure out what congruence class 1_000_000_000 is in
i=1
temp = dc(g)
loads = dd(list)
while True:
    i+=1
    temp = cycle(temp)
    l = load(temp)
    loads[l].append(i)
    
    # idk make sure we've seen it a few times...
    if len(loads[l])>3:
        cycleGuess = loads[l][-1]-loads[l][-2]
        temp2 = dc(temp)
        vals = []
        for _ in range(cycleGuess):
            temp2 = cycle(temp2)
            vals.append(load(temp2))

        # not actually convinced this is right in general,
        # but don't really wanna think about it anymore
        if l == vals[-1]:
            # probably a cycle
            B = vals[(1_000_000_000-i)%cycleGuess]
            break


print('Part A Solution:', load(north))
print('Part B Solution:', B)