from utils import *

inp = get_input(2017,23)


regs = dd(int)

ind=0
alpha_str = 'abcdefghijklmnopqrstuvwxyz'
mul_ct = 0

def parse_cmd(cmd):
    global ind
    global mul_ct
    
    cmd = cmd.split(' ')
    
    rule = cmd[0]

    if rule == 'set':
        if cmd[2] in alpha_str:
            regs[cmd[1]] = regs[cmd[2]]
        else:
            regs[cmd[1]]=int(cmd[2])
        ind+=1

    if rule == 'sub':
        if cmd[2] in alpha_str:
            regs[cmd[1]]-=regs[cmd[2]]
        else:
            regs[cmd[1]]-=int(cmd[2])
        ind+=1
    if rule == 'mul':  
        if cmd[2] in alpha_str:
            regs[cmd[1]]*=regs[cmd[2]]
        else:
            regs[cmd[1]]*=int(cmd[2])
        ind+=1
        mul_ct+=1
            
    if rule == 'jnz':
        if cmd[1] in alpha_str:
            x = regs[cmd[1]]
        else:
            x = int(cmd[1])
        if cmd[2] in alpha_str:
            y = regs[cmd[2]]
        else:
            y = int(cmd[2])
        
        
        if x!=0:
            ind+=y
        else:
            ind+=1

## A
while ind>=0 and ind<len(inp):
    parse_cmd(inp[ind])  
ans_A = int(mul_ct)
            
## B
# Sat down and figured this out by hand on paper.
# program sets b,c then
# program runs from b to c in steps of 17,
# adding 1 to h if the value is composite
# all the rest is brutally checking the primality of each value
# I'll use Miller-Rabin instead!

ind = 0 
regs = dd(int)
regs['a'] = 1
while ind<9:
    parse_cmd(inp[ind])
b = regs['b']
c = regs['c']

ans_B = 0

for i in range(b,c+1,17):
    if not miller_rabin(i):
        ans_B+=1



print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)