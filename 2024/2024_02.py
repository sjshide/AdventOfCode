from utils import *

inp = get_input(2024,2)

def isSafe(report):
    sRep = sorted(report)
    check = 0
    if (report==sRep) or (report==sRep[::-1]):
        check = 1
        for i in range(len(report)-1):
            if not (0<abs(report[i]-report[i+1])<4):
                check=0
    return(check)

A=0
B=0
for x in inp:
    l = [int(t) for t in x.split()]
    
    safeCheck = isSafe(l)
    
    # A
    A+=safeCheck
    
    # B
    for i in range(len(l)):
        safeCheck=max(safeCheck,isSafe(l[:i]+l[i+1:]))
    B+=safeCheck



print('Part A Solution:', A)
print('Part B Solution:', B)