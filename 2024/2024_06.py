from utils import *

inp = get_input(2024,6)

# mad slow. thought for a bit about how to speed it up but wasn't 
# really successful...

for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j]=='^':
            guardLoc = (i,j)

g = grid2dict(inp)
g[guardLoc]='.'

 
# A, also use visited for B
visited = set()
currPos = tuple(guardLoc)
step = (-1,0)
stepIm = -1+0j
while True:
    visited.add(currPos)
    nextPos = (currPos[0]+step[0],currPos[1]+step[1])
    # if we hit the end of the grid, quit
    if not nextPos in g:
        break
    # if you can step forward, do it
    elif g[nextPos]=='.':
        currPos = tuple(nextPos)
    # otherwise, turn
    else:
        stepIm*=(0-1j)
        step = (stepIm.real,stepIm.imag)
A = len(visited)


# do the same thing setting each position in visited to '#'.
G=dc(g)
full_visited = dc(visited)
B = 0
i = 0
for x in full_visited:
    # this is so slow: lets print some statuses
    if not i%500:
        print(i,'/',len(full_visited))
    i+=1
    visited = set()
    currPos = tuple(guardLoc)
    stepIm = -1+0j
    step = (stepIm.real,stepIm.imag)
    visited.add((currPos,step))
    
    if x!=guardLoc:
        g = dc(G)
        g[x]='#'
        while True:
            nextPos = (currPos[0]+step[0],currPos[1]+step[1])
            while g[nextPos]=='.':
                currPos=tuple(nextPos)
                nextPos = (currPos[0]+step[0],currPos[1]+step[1])
                if not nextPos in g:
                    break
            
            if (nextPos,step) in visited:
                B+=1
                break
            
            elif not nextPos in g:
                break
                
            elif g[nextPos]=='.':
                visited.add((nextPos,step))
                currPos = tuple(nextPos)
            else:
                visited.add((nextPos,step))
                stepIm = stepIm*(0-1j)
                step = (stepIm.real,stepIm.imag)

print('Part A Solution:', A)
print('Part B Solution:', B)