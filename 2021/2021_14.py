from utils import *


# not sure I handled the non-double-counted first and last character correctly here in general,
# gives the right answer for mine tho....
# might think about it a bit more and confirm.

# typo on A cost me leaderboard :(
# B much slower.

inp = get_input(2021,14)

start = inp[0]
first, last = start[0], start[-1]

ins = dict()
for x in inp[2:]:
    key, val = x.split(' -> ')
    ins[key]=val

all_lets = set()
for x in ins:
    all_lets = all_lets.union(set(x))
    
all_lets = all_lets.union(set(start))
    
def step(curr):
    global ins
    
    new_curr = dd(int)
    
    for x in curr:
        if x in ins:
            new_curr[x[0]+ins[x]]+=curr[x]
            new_curr[ins[x]+x[1]]+=curr[x]
        else:
            new_curr[x]+=curr[x]
            
    return(new_curr)


def curr2val(curr):
    global all_lets
    global first
    global last
    
    cts = dd(int)
    for l in all_lets:
        for key in curr:
            cts[l]+=(key.count(l)*curr[key])
        if l in [first,last]:
            cts[l]+=1
    return((max(cts.values())-min(cts.values()))//2)



counts = dd(int)

for i in range(len(start)-1):
    counts[start[i:i+2]]+=1

for j in range(40):
    if j == 10:
        A = curr2val(counts)

    counts = step(counts)
    
B = curr2val(counts)    
    

print('Part A Solution:', A)
print('Part B Solution:', B)