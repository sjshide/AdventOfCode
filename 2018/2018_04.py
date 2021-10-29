from utils import *

inp = sorted(get_input(2018,4))


guards = dict()

for x in inp:
    if 'Guard #' in x:
        idno = int(x.split('#')[1].split(' ')[0])
    
        if idno not in guards:
            guards[idno] = [0]*60
        last_time=0
    else:
        new_time = int(x.split(':')[1][:2])
        if 'asleep' in x:
            last_time=new_time
        else:
            for i in range(last_time,new_time):
                guards[idno][i]+=1
            last_time=new_time
            
#A
best_id = -1
most_sleep = -1
common_min = -1
for idno in guards:
    this = sum(guards[idno])
    if this>most_sleep:
        best_id = idno
        most_sleep = sum(guards[idno])
        common_min = guards[idno].index(max(guards[idno]))    
A = best_id*common_min


#B
best_id = -1
most_sleep = -1
common_min = -1
for idno in guards:
    this = max(guards[idno])
    if this>most_sleep:
        best_id = idno
        most_sleep = max(guards[idno])
        common_min = guards[idno].index(max(guards[idno]))      
B = best_id*common_min


print('Part A Solution:', A)
print('Part B Solution:', B)