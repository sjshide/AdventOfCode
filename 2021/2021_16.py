from utils import *

# just bashed it out. 146/136
# nothing fancy just a grind
# almost a miracle I didn't have typos


inp = get_input(2021,16)

binary = ''
for x in inp:
    a = int(x,16)
    b = bin(a)[2:]
    while len(b)<4:
        b = '0'+b
    binary+=b
        
A = 0

def parse_packet(s):
    global A
    
    vers = s[:3]
    
    A+=int(vers,2)
    
    type_id = s[3:6]
    
    if type_id == '100': # literal
        i = 6
        bit_grps = []
        while s[i]!='0':
            bit_grps.append(s[i:i+5])
            i+=5
            
        bit_grps.append(s[i:i+5])
        
        unused = s[i+5:]
        
        lit = ''
        for x in bit_grps:
            lit+=x[1:]
            
        return(int(lit,2), unused)
        
        
    else:   # operator on subpackets
        length_type_id = s[6]
        
        val_array = []   # keep track of values output by subpackets
        
        if length_type_id=='0': # bit length of packets given
            
            bit_length = int(s[7:7+15],2)
            
            unused = s[22:22+bit_length]
            
            while unused:
                val, unused = parse_packet(unused)
                val_array.append(val)
            
            remainder = s[22+bit_length:]
 
        else:  # number of direct subpackets given
        
            packet_number = int(s[7:7+11],2)
            
            unused = s[18:]
            
            while packet_number:
                val, unused = parse_packet(unused)
                val_array.append(val)
                packet_number-=1
                    
            remainder = unused

        # operations
        if type_id == '000':   # sum
            ret = 0
            for x in val_array:
                ret+=x
        
        elif type_id == '001': # product
            ret = 1
            for x in val_array:
                ret*=x
                
        elif type_id =='010': # min
            ret= min(val_array)
            
        elif type_id =='011': # max
            ret = max(val_array)
            
        elif type_id =='101': # greater than
            ret = int((val_array[0]>val_array[1]))
            
        elif type_id =='110': # less than
            ret = int((val_array[0]<val_array[1]))  
            
        elif type_id =='111': # equals
            ret = int(val_array[0]==val_array[1])
            
            
        return(ret,remainder)
    
B = parse_packet(binary)[0]

print('Part A Solution:', A)
print('Part B Solution:', B)
