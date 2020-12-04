from utils import *

## this is the kind of problem where my instinct is to just hack away
## would be a lot better if I was able to use regex in any meaningfully quick way
## don't have the heart to rewrite this from my hacky trash
## hope it doesn't come back to bite me


inp = get_input(2020,4)


##### recombine splits on newlines into single lines:
this = ''
inp2 = []
for x in inp:
    if x == '':
        inp2.append(this)
        this=''
    else:
        this+=x
        this+=' '
if this:
    inp2.append(this)

    
# possible key combos for valid passports
target1 = sorted(['byr','iyr','eyr','hgt','hcl','ecl','pid','cid'])    
target2 = sorted(['byr','iyr','eyr','hgt','hcl','ecl','pid'])


def valid1(p):
    x = p.split(" ")

    asdf = sorted([k.split(':')[0] for k in x])[1:] ### get rid of extra ''

    if asdf==target1 or asdf==target2:
        return(1)
    return(0)
 
    
def valid2(p):
    m = p.split(' ')
    m.remove('')
    d = dict()
    for x in m:
        l = x.split(':')
        d[l[0]]=l[1]
        
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
    if this[0]=='#':
        if len(this)==7:
            if this[1] in s:
                if this[2] in s:
                    if this[3] in s:
                        if this[4] in s:
                            if this[5] in s:
                                if this[6] in s:
                                    check+=1 ###lol omg
    ## ecl:
    this = d['ecl']
    if this in ['amb', 'blu', 'brn','gry','grn','hzl','oth']:
        check+=1
    
    
    #pid
    this = d['pid']
    lc = 0
    for m in this:
        if m in '0123456789':
            lc+=1
    if lc==9:
        check+=1
    
    
    if check==7:
        return(1)
    return(0)    


ct_A = 0
ct_B = 0

for passport in inp2:
    if valid1(passport):
        ct_A+=1
        if valid2(passport):
            ct_B+=1


print('Part A Solution:', ct_A)
print('Part B Solution:', ct_B)