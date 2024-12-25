from utils import *
from functools import lru_cache

inp = get_input(2024,19)

patterns = inp[0].split(', ')

# sort patterns by length then usual sort
# used this to help debug but why not
def ck(str):
    return len(str),str
patterns = sorted(patterns,key=ck)

@lru_cache
def possible(s):
    if s=='':
        return(0)
    elif s in patterns:
        return(1)
    else:
        t = [possible(s[i:]) for i in range(1,9) if s[:i] in patterns]
        if t:
            return(max(t))
        else:
            return(0)
        
@lru_cache
def count(s):
    if s=='':
        return(0)
    elif s in patterns and len(s)==1:
        return(1)
    elif s in patterns:
        # longest pattern is length 8 in my input, which where the 9 comes from
        # this was my bug for a while: had 8 instead of 9 below
        # classic unforced off by 1 error
        # surprisingly didn't affect A
        return(1+sum([count(s[i:]) for i in range(1,9) if s[:i] in patterns]))
    else:
        t = [count(s[i:]) for i in range(1,9) if s[:i] in patterns]
        if t:
            return(sum(t))
        else:
            return(0)

A = 0
B = 0
for x in inp[2:]:
    A+=possible(x)
    B+=count(x)

print('Part A Solution:', A)
print('Part B Solution:', B)