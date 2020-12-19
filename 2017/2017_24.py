from utils import *
from copy import deepcopy as dc

inp = get_input(2017,24)

best_len = -1

longest_paths = []


vals = dd(list)
keytoind = dict()

for i in range(len(inp)):
    a,b = [int(x) for x in inp[i].split('/')]
    
    vals[i].append((a,b))
    vals[i].append((b,a))
    keytoind[(a,b)]=i
    keytoind[(b,a)]=i
    


def best_A(path,avail):
    last = path[-1]
    
    if (last, tuple(sorted(list(avail)))) in memo:
        return(memo[(last, tuple(sorted(list(avail))))])
    
    if len(avail)==0:
        memo[(last, tuple(sorted(list(avail))))]=sum(path)
        return(sum(path))
    
    elif len(avail)==1:
        memo[(last, tuple(sorted(list(avail))))] = (sum(path)+sum([vals[x][0] for x in avail]))
        return(sum(path)+sum([vals[x][0] for x in avail]))

    
    else:
        local_avail = [vals[i][j] for j in [0,1] for i in avail
                      if vals[i][j][0]==last]

        this = [best_A(path+list(x),avail-set([keytoind[x]])) for x in local_avail]
        if not this:
            memo[(last, tuple(sorted(list(avail))))]=sum(path)
            return(sum(path))
        else:
            memo[(last, tuple(sorted(list(avail))))]=max([best_A(path+list(x),avail-set([keytoind[x]])) for x in local_avail])
            return max([best_A(path+list(x),avail-set([keytoind[x]])) for x in local_avail])


def best_B(path, avail):
    global longest_paths
    global best_len
    if len(path)==best_len:
        longest_paths.append(path)
    last = path[-1]
    
    if (last, tuple(sorted(list(avail)))) in memo:
        return(memo[(last, tuple(sorted(list(avail))))])
    
    if len(avail)==0:
        memo[(last, tuple(sorted(list(avail))))]=len(path)
        return(len(path))
    
    elif len(avail)==1:
        memo[(last, tuple(sorted(list(avail))))] = (len(path)+2)
        return(len(path)+2)

    
    else:
        local_avail = [vals[i][j] for j in [0,1] for i in avail
                      if vals[i][j][0]==last]

        this = [best_B(path+list(x),avail-set([keytoind[x]])) for x in local_avail]
        if not this:
            memo[(last, tuple(sorted(list(avail))))]=len(path)
            return(len(path))
        else:
            memo[(last, tuple(sorted(list(avail))))]=max([best_B(path+list(x),avail-set([keytoind[x]])) for x in local_avail])
            return max([best_B(path+list(x),avail-set([keytoind[x]])) for x in local_avail])
        

        
# A
memo = dict()
path = [0]
avail = set(range(len(inp)))

ans_A = best_A(path,avail)


# B
memo = dict()
path = [0]
avail = set(range(len(inp)))

best_len = best_B(path,avail)

memo = dict()
path = [0]
avail = set(range(len(inp)))
best_B(path,avail)


ans_B = max([sum(path) for path in longest_paths])

            


print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)