from utils import *

inp = get_input(2023,13)
localinp = []
patterns = dict()
ct = 0
for x in inp:
    if x:
        localinp.append(x)
    else:
        patterns[ct]=localinp
        ct+=1
        localinp=[]
        
patterns[ct]=localinp   


# count different characters in two rows of same length
def diff(p1,p2):
    ct = 0
    for x in range(len(p1)):
        ct+=(p1[x]!=p2[x])
    return(ct)

# flip a pattern across diagonal
def flip(p):
    flip = []
    for i in range(len(p[0])):
        flip.append(''.join([p[j][i] for j in range(len(p))]))
    return(flip)

# find valid mirrors
# we'll assume precisely 1 for each part of each problem
def findMirror(pattern, smudgeCt):
    for i in range(1,len(pattern)):
        flipCheck=0
        # test for mirror at i-.5
        j=1
        while i-j>0 and i+j-1<len(pattern)-1:
            if pattern[i-j]==pattern[i+j-1]:
                j+=1
            elif smudgeCt==1 and flipCheck==0 and diff(pattern[i-j],pattern[i+j-1])==1:
                flipCheck=1
                j+=1
            else:
                break
                
        if i-j==0 or i+j-1==len(pattern)-1:
            if flipCheck==1 and pattern[i-j]==pattern[i+j-1]:
                return(i)
            elif flipCheck==0 and diff(pattern[i-j],pattern[i+j-1])==smudgeCt:
                return(i)
    return(0)


A, B = 0, 0
for x in patterns:
    A += 100*findMirror(patterns[x],0)
    A += findMirror(flip(patterns[x]),0)
    B += 100*findMirror(patterns[x],1)
    B += findMirror(flip(patterns[x]),1)
    


print('Part A Solution:',A)
print('Part B Solution:',B)