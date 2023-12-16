from utils import *

inp = get_input(2023,15)

def h(s):
    curr = 0
    for c in s:
        o = ord(c)
        curr = ((curr+o)*17)%256
    return(curr)

A = 0
for x in inp.split(','):
    A+=h(x)

boxes = dict()
for i in range(256):
    boxes[i]=[]
    
for step in inp.split(','):
    if '-' in step:
        label = step[:-1]
        box = h(label)
        lenses = boxes[box]
        labels = [lens[0] for lens in lenses]
        if label in labels:
            ix = labels.index(label)
            boxes[box]=lenses[:ix]+lenses[ix+1:]
            
    else: # '=' in step
        label, fl = step.split('=')
        fl = int(fl)
        box = h(label)
        lenses = boxes[box]
        labels = [lens[0] for lens in lenses]
        if label in labels:
            ix = labels.index(label)
            boxes[box]=lenses[:ix]+[[label,fl]]+lenses[ix+1:]
        else:
            boxes[box].append([label,fl])
            
B = 0
for box in range(256):
    contents = boxes[box]
    for i in range(len(contents)):
        fl = contents[i][1]
        B+=((box+1)*(i+1)*fl)
    
    
print('Part A Solution:', A)
print('Part B Solution:', B)