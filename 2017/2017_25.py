from utils import *

inp = get_input(2017,25)

rules = dd(list)

def parse_block(c):
    state = c[0][-2]
    
    val = int(c[1][-2])
    write = int(c[2][-2])
    if 'right.' == c[3].split(' ')[-1]:
        dif = 1
    else:
        dif = -1
    new_state = c[4][-2]
    rules[(state,val)] = (write, dif, new_state)
    
    val = int(c[5][-2])
    write = int(c[6][-2])
    if 'right.' == c[7].split(' ')[-1]:
        dif = 1
    else:
        dif = -1
    new_state = c[8][-2]
    rules[(state,val)] = (write, dif, new_state)



def step(state,ind):
    this_state=state
    this_ind=ind
    
    this_val = tape[this_ind]
    write, dif, new_state = rules[(this_state,this_val)]
    
    tape[this_ind]=write
    this_ind+=dif
    
    return(new_state, this_ind)
    
    
    
for i in range(3,62,10):
    parse_block(inp[i:i+10])

    
tape = dd(int)
ind = 0
state = inp[0][-2]
steps = int(inp[1].split(' ')[-2])

for _ in range(steps):
     state,ind = step(state,ind)


ans_A = 0
for x in tape:
    ans_A+=tape[x]


print('Part A Solution:', ans_A)
print('Part B Solution:', 'Click the link on the page!')