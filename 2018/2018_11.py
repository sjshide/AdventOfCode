from utils import *

inp = get_input(2018,11)
srl = int(inp)


grid = []
for _ in range(300):
    grid.append([0]*300)
    
    
for x in range(300):
    for y in range(300):
        
        rack_id = x+11
        pl = rack_id*(y+1)
        pl+=srl
        pl*=rack_id
        pl = pl//100
        pl -= (10*(pl//10))
        pl-=5
        
        grid[y][x]=pl
        
        
# A
bestsum = -pow(10,10)
bestxy = [-1,-1]
for x in range(300-3):
    current_sum = 0
    for i in range(3):
        current_sum += sum(grid[i][x:x+3])
    if current_sum>bestsum:
        bestsum = current_sum
        bestxy=[x+1,1]
        
    
    for y in range(1,300-3):
        current_sum-=sum(grid[y-1][x:x+3])
        current_sum+=sum(grid[y+2][x:x+3])
        if current_sum>bestsum:
            bestsum = current_sum
            bestxy=[x+1,y+1]


            
#B

#not crazy fast, but a lot better than the naive implementation
bestsum = -pow(10,10)
bestxyl = [-1,-1,-1]

for size in range(1,300):
    for x in range(300-size):
        current_sum = 0
        for i in range(size):
            current_sum += sum(grid[i][x:x+size])
        if current_sum>bestsum:
            bestsum = current_sum
            bestxyl=[x+1,1,size]

        for y in range(1,300-size):
            current_sum-=sum(grid[y-1][x:x+size])
            current_sum+=sum(grid[y+size-1][x:x+size])
            if current_sum>bestsum:
                bestsum = current_sum
                bestxyl=[x+1,y+1,size]
                



print('Part A Solution:',str(bestxy[0])+','+str(bestxy[1]))
print('Part B Solution:',str(bestxyl[0])+','+str(bestxyl[1])+','+str(bestxyl[2]))