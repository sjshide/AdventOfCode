from utils import *

inp = get_input(2023,24)

# Grassmannian Fact: 4 skew lines in 3-space are intersected by exactly 2 lines 
# (thanks Jay + Eisenbud/Harris)
# Live, I wrote down the parameterization (x, Ax+B, Cx+D)
# Then setting this equal for 4 of the hailstones, I got 4 equations
# which I then tried to plug into wolframalpha to solve for A,B,C,D
# Unfortunately, this hits the character limit, so I got a free trial of Mathematica which worked
# This spits out the above 2 lines, only one of which has reasonable coefficients
# Picked this one (plus eventually figured out that I had a sign error
# from choices I'd made for printing the equations to plug in :o )
# Then with A,B,C,D in hand, I solved for the time of intersection for 2 hailstones, which then
# let me solve for the velocity and finally the starting position of the desired rock
# this took me basically all day for some reason...

# With later reflection, I realized that the parameterization (t, px + tvx, py + tvy, pz + tvz)
# while, having more variables / equations, avoids a bunch of annoying divisions that I had to deal with
# plus has the added benefit that it makes it clear that you only need 3 hailstones, plus 
# wolfram outright spits out the starting position
# This would've made my life much easier live.

# I won't do any of that here. Instead I'll try the JWolf Method.
# p + tv = p_i+tv_i
# p + sv = p_j+sv_j
# If a component of the velocities is equal,say V, then for that component
# v = (pi-pj)/(t-s) + V
# Assuming integer times, this means t-s is a divisor of pi-pj
# Run over options for these divisors, and it turns out there's unique velocities that work
# Then, take a nonequal component and solve for t and finally for the starting position

from functools import reduce

# get +/- divisors of n
# copied from stackexchange cause I don't wanna think
def factors(n):   
    n=abs(n)
    t =  set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    for x in list(t):
        t.add(-x)
    return(t)

stones = []
for x in inp:
    p, v = x.split('@')
    px,py,pz = [int(t) for t in p.split(', ')]
    vx,vy,vz = [int(t) for t in v.split(', ')]
    stones.append((px,py,pz,vx,vy,vz))
       
# A
A=0
for i in range(len(stones)-1):
    for j in range(i+1,len(stones)):
        s1 = stones[i]
        x1,y1,vx1,vy1 = [s1[t] for t in [0,1,3,4]]
        s2 = stones[j]
        x2,y2,vx2,vy2 = [s2[t] for t in [0,1,3,4]]
        # Solve for intersection point:
        # Write p1 + tv1 = p2 + sv2
        # Crossing with v2:
        # t = (p2-p1)xv2 / v1xv2
        # s = (p1-p2)xv1 / v2xv1
        
        tNum = (x2-x1)*vy2 - (y2-y1)*vx2
        sNum = (x1-x2)*vy1 - (y1-y2)*vx1
        den = vx1*vy2-vx2*vy1
        
        # for my input, parallel stones didn't intersect
        if den!=0:
            t = tNum/den
            s = sNum/(-den)
            
            if t>=0 and s>=0:
                if 200000000000000<=x1+t*vx1<=400000000000000:
                    if 200000000000000<=y1+t*vy1<=400000000000000: 
                        A+=1

# B
# get x,y,z velocities that appear more than once
xs = dd(list)
ys = dd(list)
zs = dd(list)
for i in range(len(stones)):
    s = stones[i]
    xs[s[3]].append(i)
    ys[s[4]].append(i)
    zs[s[5]].append(i)
xd = [t for t in xs if len(xs[t])>1]
yd = [t for t in ys if len(ys[t])>1]
zd = [t for t in zs if len(zs[t])>1]

# run over each component, finding the velocity
V = []
for k in range(3):
    coord = [xd,yd,zd][k]
    vals = [xs,ys,zs][k]
    t = set(range(-100000,100000))
    for a in coord:
        m = vals[a]
        for i in range(len(m)-1):
            for j in range(i+1,len(m)):
                si = stones[m[i]]
                sj = stones[m[j]]
                divs = set([a+k for k in factors(abs(si[k]-sj[k]))])
                t = t.intersection(divs)

        if len(t)==1:
            v = t.pop()
            V.append(v)
            break
            
# si, sj are two guys with v_z equal. 
# let's use this to find times:
# diff in times (t-s) = (si[2]-sj[2])/(v[2]-s[i][5])
# Just wrote this stuff down on paper.
# Name a,b,c,d for ease (just algebra though)
# a = t-s
# b = ct + ds: equation from first coord
# solve for t

a = (si[2]-sj[2])//(V[2]-si[5])

# This assumes that the x velocities aren't equal for the 
# si,sj we ended on. Seems safe but could have issues in general
b = si[0]-sj[0]
c = V[0]-si[3]
d = sj[3]-V[0]
t = (d*a+b)//(c+d)

# Get where the stones meet at time t, then find initial position of rock
# Sum of coords of P is the desired answer
meet = (si[0]+t*si[3],si[1]+t*si[4],si[2]+t*si[5])
P = [meet[i]-t*V[i] for i in range(3)]

print('Part A Solution:', A)
print('Part B Solution:', sum(P))