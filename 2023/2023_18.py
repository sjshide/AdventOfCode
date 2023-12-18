from utils import *

inp = get_input(2023,18)

# Did the brute force way for A originally.
# Obviously needed something better for B, and was 
# keyed up to use "area of a polygon" trick that some people
# used for the pipe day earlier in the year (10?)

# I guess this is shoelace formula + Pick's theorem?
# Definitely a good one to keep in mind in the future

def area(verts):
    # Assume first, last vertex the same
    # So closed polygon
    a = 0
    for i in range(len(verts)-1):
        a+=verts[i][1]*verts[i+1][0]
        a-=verts[i][0]*verts[i+1][1]
    return(abs(a))

# A
y,x = 0,0
verts = [(0,0)]
edgeCt = 0
for row in inp:
    d, steps, col = row.split()
    steps = int(steps)
    if d=='U':
        dy,dx=-1,0
    elif d=='L':
        dy,dx=0,-1
    if d=='D':
        dy,dx=1,0
    elif d=='R':
        dy,dx=0,1  

    y,x = y+steps*dy, x+steps*dx
    verts.append((y,x))
    edgeCt+=steps
    
a = area(verts)
interior = int(a/2+1-edgeCt/2)
A = edgeCt+interior
    
    
# B
y,x = 0,0
verts = [(0,0)]
edgeCt = 0
for row in inp:
    d, steps, col = row.split()
    steps = int(col[2:7],16)
    d = col[7]
    if d=='3':
        dy,dx=-1,0
    elif d=='2':
        dy,dx=0,-1
    if d=='1':
        dy,dx=1,0
    elif d=='0':
        dy,dx=0,1  

    y,x = y+steps*dy, x+steps*dx
    verts.append((y,x))
    edgeCt+=steps
    
a = area(verts)
interior = int(a/2+1-edgeCt/2)
B = edgeCt+interior
    
print('Part A Solution:', A)
print('Part B Solution:', B)
