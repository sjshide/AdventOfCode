from utils import *

inp = [int(x) for x in get_input(2020,9)]

## who needs elegant solutions when you can brutalize the problem?

ans_A = 0
for i in range(25,len(inp)):
    test = inp[i-25:i]
    check = 0
    for x in test:
        for y in test:
            if x+y==inp[i]:
                check=1
    if check==0:
        ans_A = inp[i]
        break

        
def part_B():
    l = 2
    while True:
        for i in range(0,1000-l):
            if sum(inp[i:i+l])==ans_A:
                return(max(inp[i:i+l])+min(inp[i:i+l]))
        l+=1


print('Part A Solution:', ans_A)
print('Part B Solution:', part_B())