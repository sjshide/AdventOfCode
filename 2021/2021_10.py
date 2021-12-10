from utils import *

inp = get_input(2021,10)

pairs = {'}':'{', ']':'[', '>':'<', ')':'('} 

A = 0

pts_A = {')':3,']':57, '}':1197, '>':25137}
pts_B = {'(':1,'[':2, '{':3, '<':4}

def ps(remaining):
    global pts_B
    
    cur=0
    for l in remaining:
        cur*=5
        cur+=pts_B[l]

    return(cur)


uncorrupt = []
for x in inp:
    q = []
    check = 1
    for l in x:
        if l in '{(<[':
            q.append(l)
        else:
            last = q.pop(-1)
            if pairs[l]!=last:
                A+=pts_A[l]
                check=0
                break
    if check:
        uncorrupt.append(q)


scores = []
for x in uncorrupt:
    scores.append(ps(x[::-1]))
    
B = sorted(scores)[len(scores)//2]

print('Part A Solution:', A)
print('Part B Solution:', B)