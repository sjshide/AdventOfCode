from utils import *

inp = get_input(2024,4)

g = grid2dict(inp,dd(str))

A = 0
B = 0
step = [-1,0,1]
for i in range(len(inp)):
    for j in range(len(inp[0])):
        # A
        for dy in step:
            for dx in step:
                locS = ''
                for k in range(4):
                    locS+=g[(i+k*dy,j+k*dx)]
                if locS=='XMAS':
                    A+=1
        # B
        d1 = g[(i-1,j-1)]+g[(i,j)]+g[(i+1,j+1)]
        if d1=='MAS' or d1=='SAM':
            d2 = g[(i-1,j+1)]+g[(i,j)]+g[(i+1,j-1)]
            if d2=='MAS' or d2=='SAM':
                B+=1                    
        
print('Part A Solution:', A)
print('Part B Solution:', B)