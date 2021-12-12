from utils import *

inp = get_input(2021,11)

octs = grid2dict(inp)

for x in octs:
    octs[x]=int(octs[x])
    
flashcount = 0
alldone = 0
    
def step(grid):
    global flashcount
    global alldone
    
    flashed = dd(int)
    
    for spot in grid:
        grid[spot]+=1
    
    while True:
        new_flashed=dc(flashed)
        for (y,x) in grid:
            if not new_flashed[(y,x)] and grid[(y,x)]>9:
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if (dy,dx)!=(0,0) and (y+dy,x+dx) in grid:
                            grid[(y+dy,x+dx)]+=1
                new_flashed[(y,x)]=1
                flashcount+=1
        if new_flashed ==flashed:
            break
        flashed=new_flashed
    

    flashed_this_turn=0
    for spot in flashed:
        if flashed[spot]:
            grid[spot]=0
            flashed_this_turn+=1
            
    if flashed_this_turn==len(grid):
        alldone=1
                        
    return(grid)

rounds = 0
while not alldone:
    rounds+=1
    octs = step(octs)
    
    if rounds==100:
        A = flashcount

B = rounds



print('Part A Solution:', A)
print('Part B Solution:', B)