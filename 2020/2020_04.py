from utils import *

## this is the kind of problem where my instinct is to just hack away
## would be a lot better if I was able to use regex in any meaningfully quick way
## don't have the heart to rewrite this from my hacky trash
## hope it doesn't come back to bite me
## will make minor improvements over whatever garbage I wrote first maybe


inp = get_input(2020,4)


##### parse as dicts into inp2:
d = dict()
inp2 = []
for x in inp:
    if x == '':
        inp2.append(d)
        d=dict()
    else:
        for kv_pair in x.split(' '):
            k,v = kv_pair.split(':')
            d[k]=v
if d:
    inp2.append(d)


# possible key combos for valid passports
target1 = set(['byr','iyr','eyr','hgt','hcl','ecl','pid','cid'])  
target2 = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])


def valid1(d):
    if d.keys() in [target1,target2]:
        return(1)
    return(0)
 
    
def valid2(d):
    check = 0
    
    #byr
    try:
        this = int(d['byr'])
        if 1920<=this and this<=2002:
            check+=1
    except:
        'omg'
    #iyr
    try:
        this = int(d['iyr'])
        if 2010<=this and this<=2020:
            check+=1
    except:
        'why'
    #eyr:
    try:
        this = int(d['eyr'])
        if 2020<=this and this<=2030:
            check+=1
    except:
        'please god'

    #hgt
    try:
        this = d['hgt']
        val = int(this[:-2])
        if this[-2:]=='in':
            if 59<=val and val<=76:
                check+=1
        elif this[-2:]=='cm':
            if 150<=val and val<=193:
                check+=1
    except:
        'stop'
        
        
    #hcl
    this = d['hcl']
    s = '0123456789abcdef'
    if (this[0]=='#') and (len(this)==7) and (set(this[1:]) <= set(s)):
        check+=1
        
        
    ## ecl:
    this = d['ecl']
    if this in ['amb', 'blu', 'brn','gry','grn','hzl','oth']:
        check+=1
    
    
    #pid
    this = d['pid']
    if len(this)==9 and set(this)<=set('0123456789'):
        check+=1
    
    
    ## see if all conditions are met
    if check==7:
        return(1)
    return(0)    


ct_A = 0
ct_B = 0

for passport in inp2:
    if valid1(passport):
        ct_A+=1
        ct_B+=valid2(passport)


print('Part A Solution:', ct_A)
print('Part B Solution:', ct_B)
