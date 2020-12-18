from utils import *

inp = get_input(2017,15)

# very slow. will maybe come back and try to speed up

## Given in problem statement.
factA = 16807
factB = 48271
mod = 2147483647

startA = int(inp[0].split(' ')[-1])
startB = int(inp[1].split(' ')[-1])

ans_A = 0
ans_B = 0

for i in range(40_000_000):
    startA = (startA*factA)%mod
    startB = (startB*factB)%mod
    
    A = ('0'*16)+bin(startA).split('b')[1]
    B = ('0'*16)+bin(startB).split('b')[1]
    
    if A[-16:]==B[-16:]:
        ans_A+=1


startA = int(inp[0].split(' ')[-1])
startB = int(inp[1].split(' ')[-1])

lA = []
step = 0
while True:
    step+=1
    startA = (startA*factA)%mod

    if startA%4==0:
        A = ('0'*16)+bin(startA).split('b')[1]
        lA.append(A[-16:])
        
    if len(lA)==5_000_000:
        break
        

lB = []
step = 0
while True:
    step+=1
    startB = (startB*factB)%mod
    
    if startB%8==0:
        B = ('0'*16)+bin(startB).split('b')[1]
        lB.append(B[-16:])
        
    if len(lB)==5_000_000:
        break

ans_B = 0
for i in range(5_000_000):
    if lA[i]==lB[i]:
        ans_B+=1


print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)