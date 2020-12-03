from utils import *

inp = get_input(2020,3)


# mod column by row_length to handle the "repeats to the right"
# then just count and multiply the answers

row_len = len(inp[0])

def tree_ct(slopes, row_length):
    total=1
    for m in slopes:
        x,y = m
        ct = 0
        ind = 0
        for row in inp[::y]:
            if row[ind]=='#':
                ct+=1
            ind=(ind+x)%row_length
        total*=ct
    return(total)


print('Part A Solution:', tree_ct([(3,1)],row_len))
print('Part B Solution:', tree_ct([(1,1),(3,1),(5,1),(7,1),(1,2)], row_len))