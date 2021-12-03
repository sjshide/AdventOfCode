from utils import *

inp = get_input(2021,3)


# A
# 67 global leaderboard

gam = ''
eps = ''
for i in range(len(inp[0])):
    ones = 0
    zeros = 0
    
    for x in inp:
        if x[i]=='1':
            ones+=1
        else:
            zeros+=1
    if ones>zeros:
        gam+='1'
        eps+='0'
    else:
        gam+='0'
        eps+='1'
        
A = int(gam,2)*int(eps,2)


# B
# took a while to realize I'd kept "for x in inp" below, since both still filtered down to 1....

sub = list(inp)
for i in range(len(inp[0])):
    ones = 0
    zeros = 0
    
    for x in sub:
        if x[i]=='1':
            ones+=1
        else:
            zeros+=1
    if ones>=zeros:
        dig = '1'   
    else:
        dig= '0'
        
    sub = [x for x in sub if x[i]==dig]
    
    if len(sub)==1:
        oxy = int(sub[0],2)
        
sub = list(inp)
for i in range(len(inp[0])):
    ones = 0
    zeros = 0
    
    for x in sub:
        if x[i]=='1':
            ones+=1
        else:
            zeros+=1
    if ones<zeros:
        dig = '1'   
    else:
        dig= '0'
        
    sub = [x for x in sub if x[i]==dig]
    
    if len(sub)==1:
        co2 = int(sub[0],2)
        
        
B = oxy*co2


print('Part A Solution:', A)
print('Part B Solution:', B)