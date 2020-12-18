from utils import *

inp = get_input(2017, 12)

nbs = dd(list)

for x in inp:
    brk = x.split(' <-> ')
    this = brk[0]
    nbs[this]=brk[1].split(', ')
    
def cc(node,seen = set()):
    seen.add(node)
    for x in nbs[node]:
        if x not in seen:
            new_nbs = cc(x,seen)
    return(seen)


ans_B = 0
s = list(nbs)
while s:
    this = s[0]
    a = cc(this,set())
    for x in a:
        s.remove(x)
    ans_B+=1

print('Part A Solution:', len(cc('0')))
print('Part B Solution:', ans_B)