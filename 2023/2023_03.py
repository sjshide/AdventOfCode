from utils import *

inp = get_input(2023,3)

# Process input
vals = dd(lambda:'.')
for i in range(len(inp)):
    for j in range(len(inp[i])):
        vals[(i,j)] = inp[i][j]


# For part A, keep track of symbols adjacent to a given square
# For part B, keep track of indices of *s adjacent to a given square
adjA = dd(set)
adjB = dd(set)

for y in range(len(inp)):
    for x in range(len(inp[y])):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if (dy,dx)!=(0,0):
                    if not vals[(y+dy,x+dx)].isdigit():
                        adjA[(y,x)].add(vals[(y+dy,x+dx)])
                    if vals[(y+dy,x+dx)]=='*':
                        adjB[(y,x)].add((y+dy,x+dx))
                        

# Do the calculations
A = 0
B = 0
starNums = dd(list)

for i in range(len(inp)):
    j=0
    while j<len(inp[i]):
        if not vals[(i,j)].isdigit():
            j+=1
        else:
            num = ''
            nbsA = set()
            nbsB = set()
            
            while vals[(i,j)].isdigit():
                num+=vals[(i,j)]
                
                nbsA.update(adjA[(i,j)])
                nbsB.update(adjB[(i,j)])
                
                j+=1
                
            if len(nbsA)>1:
                A+=int(num)
            for x in nbsB:
                starNums[x].append(int(num))    

# Finally, finish off B
for x in starNums:
    # Want precisely 2 numbers adjacent to the star
    if len(starNums[x])==2:
        B+=(starNums[x][0]*starNums[x][1])




print('Part A Solution:', A)
print('Part B Solution:', B)
