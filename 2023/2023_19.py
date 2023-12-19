from utils import *

inp = get_input(2023,19)

# Process input
# Handle parts in order to use solution for Part B

flows = dict()
parts = []
for x in inp:
    if x:
        if x[0]!='{': # flow
            name, rule = x.split('{')
            rule = rule[:-1]
            l = []
            for r in rule.split(','):
                if ':' in r:
                    check, target = r.split(':')
                    l.append((check[0],check[1],int(check[2:]),target))
                else:
                    l.append((r,))
            flows[name]=l

        else: # part
            t = x[1:-1]
            d = dict()
            for val in t.split(','):
                k,num = val.split('=')
                d[k]=[int(num),int(num)+1] # range with single part
            parts.append(d)

# 'part' is a range of parts here for solution to part b
# [min, max)
def process(flow, part):
    for x in part:
        if part[x][0]>=part[x][1]:
            return(0)   
    if flow=='A':
        p = 1
        for x in part:
            p*=(part[x][1]-part[x][0])
        return(p)
    elif flow == 'R':
        return(0)
    else:
        rules = flows[flow]
        for r in rules:
            if len(r)==1: # final flow
                return(process(r[0],part))
            else:
                if r[1]=='<':
                    if part[r[0]][1]<=r[2]: # all parts pass
                        return(process(r[3],part))
                    elif part[r[0]][0]>=r[2]: # all parts fail
                        continue
                    else: # split in middle
                        p1 = dc(part)
                        p2 = dc(part)
                        p1[r[0]][1]=r[2]
                        p2[r[0]][0]=r[2]
                        return(process(flow,p1)+process(flow,p2))
     
                elif r[1]=='>':
                    if part[r[0]][0]>=r[2]+1: # all parts pass
                        return(process(r[3],part))
                    if part[r[0]][1]<=r[2]+1: # all parts fail
                        continue
                    else: # split in middle
                        p1 = dc(part)
                        p2 = dc(part)
                        p1[r[0]][1]=r[2]+1
                        p2[r[0]][0]=r[2]+1
                        return(process(flow,p1)+process(flow,p2))
                    
A = 0
for x in parts:
    if process('in',x):
        for y in x:
            A+=x[y][0]
            
full = {'x':[1,4001],'m':[1,4001],'a':[1,4001],'s':[1,4001]}           

print('Part A Solution:',A)
print('Part B Solution:',process('in',full))