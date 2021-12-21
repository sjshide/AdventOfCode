from utils import *
import json

inp = get_input(2021,18)

# high quality string bash
# seems like right thing is probably some kinda binary tree?

inp = [json.loads(x) for x in inp]

def add(x,y):
    return([x,y])

def explode(num):    
    bs = []
    brackct = 0
    
    stringnum = str(num)
    
    for char in stringnum:
        if char=='[':
            brackct+=1
        elif char==']':
            brackct-=1
        bs.append(brackct) 
    
    # check if you ever hit depth 5 in the number
    if 5 not in bs:
        return(num)

    # if so, explode away
    
    ind1 = bs.index(5)
    ind2 = ind1+bs[ind1:].index(4)

    sub = stringnum[ind1:ind2+1]
    
    # always 2 regular numbers.
    # did some string garbage here live
    left, right = json.loads(sub)

    front = stringnum[:ind1+1]
    new_front = ''

    # get number to the left if it exists. at most 2 digits
    for i in range(len(front)-1,-1,-1):
        if front[i].isnumeric():
            if i > 0:
                if front[i-1].isnumeric():
                    new_front = front[:i-1]+str(int(front[i-1:i+1])+int(left))+front[i+1:]
                    break

            new_front = front[:i]+str(int(front[i])+int(left))+front[i+1:]
            break
            
    if not new_front:
        new_front=front



    # get number to the right if it exists. at most 2 digits
    back = stringnum[ind2:]
    new_back = ''
    for i in range(len(back)):
        if back[i].isnumeric():
            if i <len(back)-1:
                if back[i+1].isnumeric():
                    new_back = back[:i]+str(int(back[i:i+2])+int(right))+back[i+2:]
                    break
            new_back = back[:i]+str(int(back[i])+int(right))+back[i+1:]
            break
    if not new_back:
        new_back=back

    return(json.loads(new_front[:-1]+'0'+new_back[1:]))


def split(num):
    stringnum = str(num)
    front = ''
    for i in range(len(stringnum)-1):
        if stringnum[i:i+2].isnumeric():
            front = stringnum[:i]
            back = stringnum[i+2:]
            break
    
    # only if you find a 2 digit number
    if front:
        val = int(stringnum[i:i+2])

        new = [val//2,(val//2)+(val%2)]
        
        return(json.loads(front+str(new)+back))
    
    else:
        return(num)
    
    
def reduce(num):
    new_num = dc(num)
    
    out = []
    
    while True:
        out = explode(new_num)
        if out==new_num:
            out = split(new_num)
            
            if out==new_num: # neither operation does anything
                break
                
        new_num=dc(out)
        
    return(new_num)

def mag(num):
    if type(num[0])==int and type(num[1])==int:
        return(3*num[0]+2*num[1])
    elif type(num[0])==int and type(num[1])==list:
        return(3*num[0] + 2*mag(num[1]))
    elif type(num[0])==list and type(num[1])==int:
        return(3*mag(num[0]) + 2*num[1])
    else:
        return(3*mag(num[0]) + 2*mag(num[1]))
    
# A
first = inp[0]

for nex in inp[1:]:
    first = reduce(add(first,nex))
    
A = mag(first)   


# B
B = 0
for x in inp:
    for y in inp:
        this_mag = mag(reduce(add(x,y)))
        if this_mag>B and x!=y:
            B=this_mag

print('Part A Solution:', A)
print('Part B Solution:', B)