from utils import *

inp = get_input(2021,8)

# Digits by which segments are lit up
# caps for actual, lower for mixed up

digs = dict()

digs[0] = set('ABCEFG')
digs[1] = set('CF')
digs[2] = set('ACDEG')
digs[3] = set('ACDFG')
digs[4] = set('BCDF')
digs[5] = set('ABDFG')
digs[6] = set('ABDEFG')
digs[7] = set('ACF')
digs[8] = set('ABCDEFG')
digs[9] = set('ABCDFG')

A = 0
B = 0

for STEP in inp:
    pattern, out = STEP.split(' | ')
    
    out = out.split(' ')
    
    # count instances of the unique lengths for A
    for word in out:
        if len(word) in [2,4,3,7]:
            A+=1
    
    # mapping: mixed up to actual mapping
    mapping = dict()
    
    # counts of each segment appearance in pattern
    cts = dict()
    
    # count the number of times each letter appears in pattern
    for l in 'abcdefg':
        cts[l] = pattern.count(l)
    
    pattern = pattern.split(' ')
    
    # get the ones with unique counts
    for l in cts:
        if cts[l] == 9:
            mapping[l] = 'F'
        if cts[l] == 6:
            mapping[l] = 'B'
        if cts[l] == 4:
            mapping[l] = 'E'
    
    # do the other associations
    # probably not minimal but worked
    for word in pattern:
        if len(word)==2:
            for l in word:
                if l not in mapping:
                    mapping[l] = 'C'
                    
    for l in cts:
        if l not in mapping and cts[l] == 8:
            mapping[l] = 'A'

    for word in pattern:
        if len(word) == 4:
            for l in word:
                if l not in mapping:
                    mapping[l]='D'
    for l in cts:
        if l not in mapping:
            mapping[l] = 'G'
     
    # translate the output and add it to the total
    num = ''
    
    for n in out:
        loc = set()
        for l in n:
            loc.add(mapping[l])
        for dig in digs:
            if digs[dig]==loc:
                num+=str(dig)
                
        
    B+=int(num)

print('Part A Solution:', A)
print('Part B Solution:', B)