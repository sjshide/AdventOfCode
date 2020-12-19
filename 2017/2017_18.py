from utils import *

inp = get_input(2017,18)


regs = dd(int)

ind=0
last_played=0
rec_check = 0
alpha_str = 'abcdefghijklmnopqrstuvwxyz'

def parse_cmd_A(cmd):
    global ind
    global last_played
    global rec_check
    
    cmd = cmd.split(' ')
    
    rule = cmd[0]
    
    if rule == 'snd':
        if cmd[1] in alpha_str:
            last_played = regs[cmd[1]]
        else:
            last_played = cmd[1]
        ind+=1
    
    if rule == 'set':
        if cmd[2] in alpha_str:
            regs[cmd[1]] = regs[cmd[2]]
        else:
            regs[cmd[1]]=int(cmd[2])
        ind+=1
    
    if rule == 'add':
        if cmd[2] in alpha_str:
            regs[cmd[1]]+=regs[cmd[2]]
        else:
            regs[cmd[1]]+=int(cmd[2])
        ind+=1
    
    if rule == 'mul':  
        if cmd[2] in alpha_str:
            regs[cmd[1]]*=regs[cmd[2]]
        else:
            regs[cmd[1]]*=int(cmd[2])
        ind+=1
    
    if rule == 'mod':
        if cmd[2] in alpha_str:
            regs[cmd[1]] = regs[cmd[1]]%regs[cmd[2]]
        else:
            regs[cmd[1]] = regs[cmd[1]]%int(cmd[2])
        ind+=1
                                
    if rule == 'rcv':
        if cmd[1] in alpha_str:
            if regs[cmd[1]]!=0:
                rec_check=1
        else:
            if int(cmd[1])!=0:
                rec_check=1
        ind+=1
        
    
    if rule == 'jgz':
        if cmd[1] in alpha_str:
            x = regs[cmd[1]]
        else:
            x = int(cmd[1])
        if cmd[2] in alpha_str:
            y = regs[cmd[2]]
        else:
            y = int(cmd[2])
        
        
        if x>0:
            ind+=y
        else:
            ind+=1
            
while ind>=0 and ind<len(inp) and rec_check==0:
    parse_cmd_A(inp[ind])
ans_A = int(last_played)

regs = [dd(int),dd(int)]
regs[0]['p']=0
regs[1]['p']=1
ind = [0,0]
last_played = [0,0]
mq = [[],[]]

send_ct = [0,0]
alpha_str = 'abcdefghijklmnopqrstuvwxyz'

def parse_cmd_B(cmd,mach):
    global ind
    global last_played
    
    cmd = cmd.split(' ')
    
    rule = cmd[0]
    
    if rule == 'snd':
        if cmd[1] in alpha_str:
            mq[1-mach].append(regs[mach][cmd[1]])
        else:
            mq[1-mach].append(int(cmd[1]))
        ind[mach]+=1
        send_ct[mach]+=1
    
    if rule == 'set':
        if cmd[2] in alpha_str:
            regs[mach][cmd[1]] = regs[mach][cmd[2]]
        else:
            regs[mach][cmd[1]]=int(cmd[2])
        ind[mach]+=1
    
    if rule == 'add':
        if cmd[2] in alpha_str:
            regs[mach][cmd[1]]+=regs[mach][cmd[2]]
        else:
            regs[mach][cmd[1]]+=int(cmd[2])
        ind[mach]+=1
    
    if rule == 'mul':  
        if cmd[2] in alpha_str:
            regs[mach][cmd[1]]*=regs[mach][cmd[2]]
        else:
            regs[mach][cmd[1]]*=int(cmd[2])
        ind[mach]+=1
    
    if rule == 'mod':
        if cmd[2] in alpha_str:
            regs[mach][cmd[1]] = regs[mach][cmd[1]]%regs[mach][cmd[2]]
        else:
            regs[mach][cmd[1]] = regs[mach][cmd[1]]%int(cmd[2])
        ind[mach]+=1
                                
    if rule == 'rcv':
        if not mq[mach]:
            1
        else:
            regs[mach][cmd[1]] = mq[mach].pop(0)

            ind[mach]+=1
        
    
    if rule == 'jgz':
        if cmd[1] in alpha_str:
            x = regs[mach][cmd[1]]
        else:
            x = int(cmd[1])
        if cmd[2] in alpha_str:
            y = regs[mach][cmd[2]]
        else:
            y = int(cmd[2])
        
        
        if x>0:
            ind[mach]+=y
        else:
            ind[mach]+=1


            
            
while True:
    parse_cmd_B(inp[ind[0]],0)
    parse_cmd_B(inp[ind[1]],1)
    
    if mq==[[],[]] and 'rcv'==inp[ind[0]][:3] and 'rcv' ==inp[ind[1]][:3]:
        break
    
    
ans_B=send_ct[1]
print('Part A Solution:', ans_A)
print('Part B Solution:', ans_B)