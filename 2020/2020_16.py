from utils import *

inp = get_input(2020,16)

# break apart
fields=inp[:20]
my_ticket = [int(val) for val in inp[22].split(',')]
nearby_tickets = inp[25:]

range_dict = dict()
for x in fields:
    key,vals = x.split(': ')
    this_list = []
    for req in vals.split(' or '):
        this_list.append(tuple([int(bound) for bound in req.split('-')]))
    range_dict[key]=this_list
    
    
def check_valid(to_check,key):
    check = 0
    for x in range_dict[key]:
        if x[0]<=to_check and to_check<=x[1]:
            check=1
    return(check)


# Part A and setup for B
ans_A = 0
valid_nearby = []

for x in nearby_tickets:
    tick_flag = 0
    for this_value in [int(m) for m in x.split(',')]:
        check =0
        for key in range_dict:
            check+=check_valid(this_value,key)
        if not check:
            ans_A+=this_value
            tick_flag=1
    if not tick_flag:
        valid_nearby.append(x)

                
# Part B
# Run through all positions in ticket, ruling out all possible keys
# You're left with exactly one possible configuration
# Gotta be a cleaner way to do this, but got it done


# split to ints
vn = []
for x in valid_nearby:
    vn.append([int(t) for t in x.split(',')]) 

# get possible ticket fields for each spot in ticket
# not ruled out by nearby tickets
# so possible is (place in ticket): (pot. fields corresponding to that place)
possible = dict()
for i in range(20):
    pos = set(range_dict.keys())
    for tick in vn:
        to_remove = set()
        for key in pos:
            if not check_valid(tick[i],key):
                to_remove.add(key)
        pos-=to_remove
    possible[i]=pos

# Finally, get which spot corresponds to which place
final = dict()
accounted = set()
for i in range(20):
    for key in possible:
        if len(possible[key])==i+1:
            this_field = list(possible[key]-accounted)[0]
            final[this_field] = key
            accounted.add(this_field) 


ans_B=1
for key in final:
    if 'departure' in key:
        ans_B*=my_ticket[final[key]]


print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)
