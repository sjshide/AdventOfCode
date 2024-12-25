from utils import *
from collections import Counter

def oneStep(l):
    new = dd(int)
    for x in l:
        if x=='0':
            new['1']+=l[x]
        elif not len(x)%2:
            f = x[:len(x)//2]
            s = x[len(x)//2:]
            s=str(int(s)) # get rid of initial 0s
            new[f]+=l[x]
            new[s]+=l[x]
        else:
            new[str(int(x)*2024)]+=l[x]
    return(new)

inp = get_input(2024,11)
t = [x for x in inp.split()]
cc = Counter(t)

for i in range(75):
    cc = oneStep(cc)
    if i==24:
        A=sum([cc[x] for x in cc])
B=sum([cc[x] for x in cc])

print('Part A Solution:', A)
print('Part B Solution:', B)