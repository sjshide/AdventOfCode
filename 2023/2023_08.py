from utils import *
import numpy as np

inp = get_input(2023,8)

# Process input
inst = inp[0]
nodes = dict()
for x in inp[2:]:
    nodes[x[:3]]= (x[7:10],x[12:15])
    
# Much to r/adventofcode's chagrin,
# each A node only reaches a single Z node
# and the length it takes to reach it is the same length
# as the subsequent cycles. 
# When doing the problem live I looked at the cycle lengths
# over a bunch of iterations and then used this info
# For this we'll just assume this info.
    
aNodes = [x for x in nodes if x[2]=='A']
zNodes = [x for x in nodes if x[2]=='Z']

step=0
positions = list(aNodes)
longinst = inst*10000

cycleLens = dict()

ix = list(range(len(aNodes)))

# For each A node, step until you hit a Z node and store how long it took.
# Then only continue looking at nodes that haven't yet hit a Z
while ix:
    turn = longinst[step]
    if turn=='L':
        positions = [nodes[pos][0] for pos in positions]
    elif turn=='R':
        positions = [nodes[pos][1] for pos in positions]
    step+=1
    
    newIx = []
    for i in ix:
        if positions[i] in zNodes:
            cycleLens[aNodes[i]] = step
        else:
            newIx.append(i)
    ix = newIx

A = cycleLens['AAA']

# since I'm using python 3.8.3 lol
# 3.9 and up has math.lcm
lens = list(cycleLens.values())
B = np.lcm.reduce(lens)

print('Part A Solution:', A)
print('Part B Solution:', B)