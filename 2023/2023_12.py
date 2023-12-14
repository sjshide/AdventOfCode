from utils import *
import functools

inp = get_input(2023,12)

# function for converting symbol values to the counts
# goes until it hits a question mark.
def sym2ct(sym):
    cts = []
    hashCt = 0
    noQ = 1
    for i in range(len(sym)):
        if sym[i]=='#':
            hashCt+=1
        elif sym[i]=='.':
            if hashCt>0:
                cts.append(hashCt)
            hashCt=0
        elif sym[i]=='?':
            noQ=0
            break
    if noQ and hashCt:
        cts.append(hashCt)
    return(tuple(cts))


# For part A, did the dumbest recursion. 
# This is what I came up with for B
# Not the cleanest solution but it works. 
# Idea is memoize and strip off initial parts of the pattern that you know to be good
# a lot of this is doing that initial stripping...and handling various cases for 
# comparison to the cts after doing the stripping...
# Also originally got burned by not adding the question marks between the symbols for B
# That's why you read the instructions.

@functools.lru_cache(maxsize=None)
def process(sym, cts):
    if sym=='.':
        return((cts==(0,)) or (len((cts))==0))
    while sym[0]=='.':
        sym=sym[1:]
        if not sym:
            return(((cts==(0,)) or (len((cts))==0)))
    c = sym2ct(sym)
    if '?' not in sym:
        if c==cts:
            return(1)
        else:
            return(0)
    else:
        newSym = sym
        newCts = cts
        if len(c)>len(cts):
            return(0)
        for i in range(len(c)):
            if c[i]!=cts[i]:
                return(0)
            else:
                while newSym[0]=='.':
                    newSym=newSym[1:]
                dotIx = newSym.index('.')
                newSym = newSym[dotIx+1:]
                newCts = newCts[1:]
                
        
        ix = newSym.index('?')
        dot = newSym[:ix]+'.'+newSym[ix+1:]
        hsh = newSym[:ix]+'#'+newSym[ix+1:]
        return(process(dot,newCts)+process(hsh,newCts))

    
A, B = 0, 0
for x in inp:
    sym, cts = x.split()
    cts = tuple([int(n) for n in cts.split(',')])
    A+=process(sym,cts)
    B+=process(((sym+'?')*5)[:-1],cts*5)
    
print('Part A Solution:', A)
print('Part B Solution:', B)