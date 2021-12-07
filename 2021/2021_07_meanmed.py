from utils import *
from math import ceil,floor
import numpy as np

# Standard proof for "mean minimizes MSE" works for part b as well (with some extra bounding)
# then take ceil/floor since we need an int

inp = [int(x) for x in get_input(2021,7).split(',')]

med = np.median(inp)
avg = np.average(inp)

def tri(n):
    return(n*(n+1)//2)

A = min(sum([abs(floor(med)-x) for x in inp]), sum([abs(ceil(med)-x) for x in inp]))
B = min(sum([tri(abs(floor(avg)-x)) for x in inp]), sum([tri(abs(ceil(med)-x)) for x in inp]))

print('Part A Solution:', A)
print('Part B Solution:', B)