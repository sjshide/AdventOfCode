from utils import *

inp = get_input(2017,8)

reg_dict = dd(int)
glob_max = 0

def parse_com(command):
    sp = command.split(' ')
    global glob_max
    
    reg = sp[0]
    inc_dec = sp[1]
    change_val = int(sp[2])
    
    test_reg = sp[4]
    boo = sp[5]
    test_val = int(sp[6])
    test_reg_val = reg_dict[test_reg]

    if eval(f"""{test_reg_val} {boo} {test_val}"""):
        if inc_dec == 'inc':
            reg_dict[reg]+=change_val
        else:
            reg_dict[reg]-=change_val
            
        glob_max = max(glob_max, reg_dict[reg])
    
    return('True')

for com in inp:
    parse_com(com)

print('Part A Solution:', max([reg_dict[t] for t in reg_dict]))
print('Part B Solution:', glob_max)