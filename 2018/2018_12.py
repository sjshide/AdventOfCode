from utils import *
from copy import deepcopy as dc

inp = get_input(2018,12)

pts = dd(lambda:'.')
init = inp[0].split(': ')[1]
for i in range(len(init)):
    pts[i]=init[i]
    
rules = dict()
for x in inp[2:]:
    key, val = x.split(' => ')
    rules[key]=val

    
#A
cop_pts = dc(pts)
for _ in range(20):
    loc = dd(lambda:'.')
    for x in range(min(cop_pts.keys())-2,max(cop_pts.keys())+3):
        loc_str = ''
        for i in range(-2,3):
            loc_str+=cop_pts[x+i]
        loc[x]=rules[loc_str]
    cop_pts = loc

A = 0  
for key in cop_pts:
    if cop_pts[key]=='#':
        A+=key


        
        
# B
# I think this goes into like some kinda game-of-life-esque glider or whatever
# seems to eventually grow by a constant. so lets figure out what the constant is
# not sure how to prove that this works....

cop_pts = dc(pts)
diffs = []
this = 0
for gen in range(50_000_000_000):
    last_this=this
    loc = dd(lambda:'.')
    for x in range(min(cop_pts.keys())-2,max(cop_pts.keys())+3):
        loc_str = ''
        for i in range(-2,3):
            loc_str+=cop_pts[x+i]
        loc[x]=rules[loc_str]
    cop_pts = loc
    this = 0
    for key in cop_pts:
        if cop_pts[key]=='#':
            this+=key
    diffs.append(this-last_this)
    if len(set(diffs[-5:]))==1 and gen>5:
        const_dif = diffs[-1]
        break
        
B = this + const_dif*(50_000_000_000-gen-1)
        


print('Part A Solution:', A)
print('Part B Solution:', B)