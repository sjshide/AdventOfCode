from utils import *

inp = get_input(2020,8)

def parse(inst):
    acc = 0
    seen = set()
    ind=0
    
    while True:
        if ind==len(inst):
            return(acc,1)
        if ind in seen:
            return(acc,0)
        else:
            seen.add(ind)
            rule,val = inst[ind].split(' ')
            val=int(val)
            if rule=='acc':
                acc+=val
                ind+=1
            elif rule=='jmp':
                ind+=val
            elif rule=='nop':
                ind+=1

pt_B = 0
for i in range(len(inp)):
    loc_inp=list(inp)
    check=0
    if loc_inp[i][0:3]=='nop':
        loc_inp[i]='jmp'+loc_inp[i][3:]
        check=1
    elif loc_inp[i][0:3]=='jmp':
        loc_inp[i]='nop'+loc_inp[i][3:]
        check=1
    if check==1:
        if (parse(loc_inp)[1]):
            pt_B = parse(loc_inp)[0]


print('Part A Solution:', parse(inp)[0])
print('Part B Solution:', pt_B)