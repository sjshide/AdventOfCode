from utils import *

inp = get_input(2018,2)

#A
twos = 0
threes = 0

let_cts = dict()


# Iterate through, computing the correct thing.
for x in inp:
    d = dd(int)
    for let in x:
        d[let]+=1
    
    vals = list(d.values())
    if 2 in vals:
        twos+=1
    if 3 in vals:
        threes+=1
        
A = twos*threes


#B

# Find the index where removing 2 gives equal.
for i in range(len(inp[0])):
    s = set()
    for x in inp:
        s.add(x[:i]+x[i+1:])
    if len(s)<len(inp):
        break

# Find the duped guy.        
sub_inp = [x[:i]+x[i+1:] for x in inp]

for x in sub_inp:
    if sub_inp.count(x)==2:
        B=x
        break



print('Part A Solution:', A)
print('Part B Solution:', B)