from utils import *

inp = get_input(2020,1)

inp = [int(x) for x in inp]

#Brutal for-loop approach. Inelegant but fast enough for this short of inputs.

#A


def part_A():
    for x in inp:
        for y in inp:
            if x+y==2020:
                print('Part A Solution:', x*y)
                return
            
#B

def part_B():
    for x in inp:
        for y in inp:
            for z in inp:
                if x+y+z==2020:
                    print('Part B Solution:', x*y*z)
                    return
part_A()
part_B()