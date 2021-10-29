from utils import *
from copy import deepcopy as dc

inp = get_input(2018,7)


prereq = dd(list)
steps = set()
nec_for = dd(list)
for x in inp:
    this = x.split(' ')
    prereq[this[7]].append(this[1])
    steps.update([this[1],this[7]])
    nec_for[this[1]].append(this[7])

for x in steps:
    if x not in prereq:
        prereq[x]=[]

        
#A        
A = ''
p = dc(prereq)
s = dc(steps)
while s:
    avail = sorted([x for x in s if not p[x]])
    this=avail[0]
    A+=this
    
    for step in p:
        if this in p[step]:
            p[step].remove(this)
    s.remove(this)        

    
#B
LETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lens = dict()
for i in range(len(LETS)):
    lens[LETS[i]]=61+i

wks = [-1,-1,-1,-1]
wkr = ['','','','']

ans = ''
p = dc(prereq)
s = dc(steps)

time = 0

while s:
    avail = sorted([x for x in s if (not p[x] and x not in wkr)])
      
    for i in range(len(wkr)):
        if (not wkr[i]) and avail:
            this = avail.pop(0)
            wkr[i]=this
            wks[i]=lens[this]
    
    for i in range(len(wks)):
        if wks[i]==1:
            ans+=wkr[i]
            s.remove(wkr[i])
            for step in p:
                if wkr[i] in p[step]:
                    p[step].remove(wkr[i])
            
            wkr[i]=''
            wks[i]=-1
    
    for i in range(len(wks)):
        wks[i]-=1
        
    time+=1        
    

print('Part A Solution:', A)
print('Part B Solution:', time)