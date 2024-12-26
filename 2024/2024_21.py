from utils import *

inp = get_input(2024,21)

# this took me until the 23rd after work. 
# definitely the hardest puzzle for me this year.
# lots of different attempts and ideas eventually got to the below
# I think it's likely true that one choice is always optimal
# but my intuition for this puzzle was really struggling.
# by the time I had come up with the idea to just try all the choices,
# I had optimized everything enough that this was computationally reasonable

# live for A I just created all the possible strings
# obviously lots of optimization of this in what's below

## SETUP
# button positions
nk = dict()
nk['A'] = (3,2)
nk['0'] = (3,1)
nk['1'] = (2,0)
nk['2'] = (2,1)
nk['3'] = (2,2)
nk['4'] = (1,0)
nk['5'] = (1,1)
nk['6'] = (1,2)
nk['7'] = (0,0)
nk['8'] = (0,1)
nk['9'] = (0,2)
    
dk = dict()
dk['^'] = (0,1)
dk['A'] = (0,2)
dk['<'] = (1,0)
dk['v'] = (1,1)
dk['>'] = (1,2)
    
# paths
optsN = dict()

for a in nk:
    for b in nk:
        ax,ay = nk[a]
        bx,by = nk[b]
        
        if ax>bx:
            ud = '^'*(ax-bx)
        else:
            ud = 'v'*(bx-ax)
        if ay>by:
            lr = '<'*(ay-by)
        else:
            lr = '>'*(by-ay)
            
        optsN[(a,b)] = set([ud+lr+'A',lr+ud+'A'])
        
# remove options going into the empty square
for x in optsN:
    if x[0]=='A':
        optsN[x] = set([s for s in optsN[x] if s[:2]!='<<'])
    if x[0]=='0':
        optsN[x] = set([s for s in optsN[x] if s[:1]!='<'])
    if x[0]=='1':
        optsN[x] = set([s for s in optsN[x] if s[:1]!='v'])
    if x[0]=='4':
        optsN[x] = set([s for s in optsN[x] if s[:2]!='vv'])
    if x[0]=='7':
        optsN[x] = set([s for s in optsN[x] if s[:3]!='vvv'])   
               
optsD = dict()
for a in dk:
    for b in dk:
        ax,ay = dk[a]
        bx,by = dk[b]
        
        if ax>bx:
            ud = '^'*(ax-bx)
        else:
            ud = 'v'*(bx-ax)
        if ay>by:
            lr = '<'*(ay-by)
        else:
            lr = '>'*(by-ay)
            
        optsD[(a,b)] = set([ud+lr+'A',lr+ud+'A'])

# remove options going into the empty square
for x in optsD:
    if x[0]=='<':
        optsD[x] = set([s for s in optsD[x] if s[:1]!='^']) 
    if x[0]=='^':
        optsD[x] = set([s for s in optsD[x] if s[:1]!='<']) 
    if x[0]=='A':
        optsD[x] = set([s for s in optsD[x] if s[:2]!='<<'])   
               
# After all this, can brute force try all options for the first pad
# then on directional pads, there are only 4 paths with 2 options each
# the rest you only have one option
# just try all the combos
def processPad(S,N):
    # best length
    M = pow(10,1000)
    
    # brute forcing all the double options on directional keypad
    for o1 in set(['>vA', 'v>A']):
        for o2 in set(['<vA', 'v<A']):
            for o3 in set(['>^A', '^>A']):
                for o4 in set(['<^A', '^<A']):
                    optsD[('^', '>')]={o1}
                    optsD[('A', 'v')]={o2}
                    optsD[('v', 'A')]={o3}
                    optsD[('>', '^')]={o4}
                    
                    s='A'+S
                    level1 = set()
                    level1.add('')

                    for i in range(len(s)-1):
                        c0 = s[i]
                        n0 = s[i+1]
                        newL1 = set()
                        poss = optsN[(c0,n0)]
                        for x in poss:
                            for y in level1:
                                newL1.add(y+x)
                        level1 = newL1

                    currLevel = set(level1)
                    ds = []
                    for x in currLevel:
                        d = dd(int)
                        for i in range(len(x)):
                            d[('A'+x)[i:i+2]]+=1
                        ds.append(d)

                    for nn in range(N):       
                        last = ''
                        newDs = []
                        for d in ds:
                            newD = dd(int)
                            for x in d:
                                opts = list(optsD[(x[0],x[1])])
                                o = opts[0]
                                for i in range(len(o)):
                                    newD[('A'+o)[i:i+2]]+=(d[x])
                            newDs.append(newD)   
                        ds=newDs
                        
                    for z in ds:
                        t = sum(z[y] for y in z)
                        if t<M:
                            M=t             
    return(M)

A=0
B=0
for x in inp:
    a=processPad(x,2)
    b=processPad(x,25)
    n=int(x[:3])
    
    A+=a*n
    B+=b*n

print('Part A Solution:', A)
print('Part B Solution:', B)