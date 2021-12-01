from utils import *

inp = [int(x) for x in get_input(2021,1)]

# Got some weird timeout in my input pull, then a bunch of small goofs


#A
A = 0
for i in range(1,len(inp)):
    if inp[i]>inp[i-1]:
        A+=1

#B

B = 0
for i in range(1,len(inp)-2):
    if sum(inp[i:i+3])>sum(inp[i-1:i+2]):
        B+=1

print('Part A Solution:', A)
print('Part B Solution:', B)