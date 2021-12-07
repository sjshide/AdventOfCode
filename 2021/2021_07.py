from utils import *

inp = [int(x) for x in get_input(2021,7).split(',')]

# very janky, but was fast enough

A = pow(10,20)
B = pow(10,20)

for i in range(min(inp),max(inp)+1):
    ct_A = 0
    ct_B = 0
    for x in inp:
        ct_A+=abs(x-i)
        ct_B+=abs(x-i)*(abs(x-i)+1)//2
    if ct_A<A:
        A=ct_A
    if ct_B<B:
        B=ct_B

print('Part A Solution:', A)
print('Part B Solution:', B)