from utils import *

inp = [int(x) for x in get_input(2021,6).split(',')]


def step(d):
    new = dd(int)
    
    for x in d:
        if x==0:
            new[6]+=d[x]
            new[8]+=d[x]
        else:
            new[x-1]+=d[x]
    return(new)

def dict_ct(d):
    ct=0
    for key in d:
        ct+=d[key]
    return(ct)


fish = dd(int)

for x in inp:
    fish[x]+=1
    
this = dc(fish)

for i in range(256):
    this = step(this)
    if i==79:
        A = dict_ct(this)
B = dict_ct(this)


print('Part A Solution:', A)
print('Part B Solution:', B)