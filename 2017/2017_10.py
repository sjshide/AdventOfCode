from utils import *

inp = get_input(2017,10)
int_inp = [int(x) for x in inp.split(',')]


def knot(steps = [], length=256, init=list(range(256)), current_pos=0, skip=0):
    for step in steps:
        if current_pos+step<length:
            ind = current_pos
            ind2 = current_pos+step
            init = init[:ind]+(init[ind:ind2])[::-1]+init[ind2:]
            
        else:
            ind=current_pos
            ind2 = (current_pos+step)%length
            local = init[ind:]+init[:ind2]
            local = local[::-1]
            init = local[length-ind:]+init[ind2:ind]+local[:length-ind]

        current_pos = (current_pos+step+skip)%length
        skip+=1
        
    return(init, current_pos, skip)


def ascii_to_hex(s):
    m = hex(s)[2:]
    if len(m) == 1:
        m = '0'+m
    return(m)

def str_to_hash(s):
    steps=[ord(i) for i in s]+[17, 31, 73, 47, 23]
    init = list(range(256))
    current_pos = 0
    skip = 0
    
    for _ in range(64):
        init, current_pos, skip = knot(steps, 256, init, current_pos, skip)
        
    dense = []
    for i in range(16):
        dense_val = 0
        for m in init[16*i:16*(i+1)]:
            dense_val = dense_val^m
        dense.append(dense_val)
        
    final_hash = ''
    for x in dense:
        final_hash+=ascii_to_hex(x)
    return(final_hash)


# A
i,cp,sk = knot(int_inp)
ans_A = i[0]*i[1]
  
print('Part A Solution:', ans_A)
print('Part B Solution:', str_to_hash(inp))