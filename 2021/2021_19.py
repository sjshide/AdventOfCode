from utils import *
import numpy as np
from itertools import permutations

inp = get_input(2021,19)

# absolute brute force bash
# idea:
# for all permutations (ignored orientation live, but this worked)
# updated to include orientation check here. does run faster.
# try lining up pairs of points until you get an overlap of 12
# then shift everything to the first beacon.

# takes a really long time to run but can't think of much to simplify...
# takes about 3 minutes

# comedy of errors live - didn't parse the last beacon, so wasted a bunch of time
# then was adding shift + first point rather than just shift in part b
# shouldve taken probably half the time...



# manhattan distance
def manh(s,t):
    return(abs(s[0]-t[0])+abs(s[1]-t[1])+abs(s[2]-t[2]))

# dict with key = beacon number, val = pts seen by that beacon
pts = dict()

# split out the input
for x in inp:
    if 'scanner' in x:
        num = int(x.split(' ')[2])
        this_pts = []
    elif x:
        this_pts.append(tuple([int(t) for t in x.split(',')]))
    else:
        pts[num]=this_pts
pts[num]=this_pts   # add the last set of points!!!

# takes 2 sets of points, runs through all permutations/sign changes keeping the same orientation
# and tries to line up the sets of points
# if overlap of 12, return the shift, otherwise return False

def shift_rel(a,b):
    # a, b sets of tuples of pts
    #fix a point in a
    for ref in [np.array(t) for t in a]: 
        # run through all permutations and flips of coordinates.
        # if correct orientation, then compare point sets
        for p in permutations([0,1,2]):
            # calc perm sign:
            invs = 0
            for pair in [(0,1),(0,2),(1,2)]:
                if p[pair[0]]>p[pair[1]]:
                    invs+=1
            
            for i0 in [-1,1]:
                for i1 in [-1,1]:
                    for i2 in [-1,1]:
                        if pow(-1,invs)*i0*i1*i2==1:
                            
                            # perform the shift on pts in b
                            this_b = [np.array((i0*x[p[0]],i1*x[p[1]],i2*x[p[2]])) for x in b]

                            # try to match them to your pt in a
                            for pt in this_b:
                                shift = ref - pt
                                shifted = set([tuple(shift+opt) for opt in this_b])

                                # check if there's a 12 point overlap
                                if len(set(a).intersection(shifted))>11:
                                    return(shifted, shift)
    return((False,False))
    
    
accted_for_pts = set()
shifts = set()

# initialize with the points for beacon 0
for pt in pts[0]:
    accted_for_pts.add(pt)

to_do = list(range(1,len(pts)))
while to_do:
    print('Remaining Scanners to Account for:', len(to_do))
          
    for curr_scanner in list(to_do):
        shifted, shift = shift_rel(accted_for_pts, pts[curr_scanner])
        if shifted:
            to_do.remove(curr_scanner)
            accted_for_pts = accted_for_pts.union(shifted)
            shifts.add(tuple(shift))

A = len(accted_for_pts)

B = 0
for x in shifts:
    for y in shifts:
        if manh(x,y)>B:
            B = manh(x,y)
                            
                            
print('Part A Solution:', A)
print('Part B Solution:', B)