from utils import *

inp = get_input(2018,13)

# handle turns
rights = dict()
lefts = dict()
lefts['<']='v'
lefts['^']='<'
lefts['>']='^'
lefts['v']='>'
rights['<']='^'
rights['^']='>'
rights['>']='v'
rights['v']='<'


# define cart class
class cart:
    global lefts
    global rights
    
    def __init__(self, y, x, direction, grid):
        self.y = y
        self.x = x
        self.direction = direction ## <, >, ^, v
        self.turn = 'L' # L, S, R
        self.grid=grid
    
    def step(self):
        # find next coord
        # assumes there are no carts on corners or +s
        # gives right answers but not explicitly stated as a condition on the input
        if self.direction == '<':
            self.x-=1
        elif self.direction == '>':
            self.x+=1
        elif self.direction == '^':
            self.y-=1
        elif self.direction == 'v':
            self.y+=1
        
        # handle all the turn cases ?????
        
        # +
        if self.grid[self.y][self.x]=='+':
            if self.turn=='L':
                self.direction=lefts[self.direction]
                self.turn = 'S'
            elif self.turn=='S':
                self.turn = 'R'
            elif self.turn=='R':
                self.direction=rights[self.direction]
                self.turn='L'
        
        # /
        if self.grid[self.y][self.x]=='/':
            if self.direction in '><':
                self.direction=lefts[self.direction]
            elif self.direction in '^v':
                self.direction=rights[self.direction]
                
        # \\
        if self.grid[self.y][self.x]=='\\':
            if self.direction in '^v':
                self.direction=lefts[self.direction]
            elif self.direction in '><':
                self.direction=rights[self.direction]

def part_1(grid):
    # read in carts
    carts = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in 'v^<>':
                carts.append(cart(y,x,grid[y][x],grid))    
                
    # initialize current position dict
    curr_locs = dict()
    for this_cart in carts:
        curr_locs[(this_cart.y,this_cart.x)]=this_cart
        
    
    # run the process
    while True: 
        new_locs = dict()

        for (y,x) in sorted(list(curr_locs.keys())):
            if (y,x) in curr_locs:
                this_cart = curr_locs[(y,x)]

                this_cart.step()
                curr_locs.pop((y,x))

                if (this_cart.y,this_cart.x) in curr_locs or (this_cart.y,this_cart.x) in new_locs:
                    return((this_cart.x,this_cart.y))

                new_locs[(this_cart.y,this_cart.x)]=this_cart
                
        curr_locs=new_locs
                
def part_2(grid):
    # read in carts
    carts = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in 'v^<>':
                carts.append(cart(y,x,grid[y][x],grid))    
                
    # initialize current position dict
    curr_locs = dict()
    for this_cart in carts:
        curr_locs[(this_cart.y,this_cart.x)]=this_cart
        
    
    # run the process
    while True: 
        if len(curr_locs)==1:
            for x in curr_locs:
                last_cart = curr_locs[x]
            return((last_cart.x,last_cart.y))
        
        new_locs = dict()

        for (y,x) in sorted(list(curr_locs.keys())):
            if (y,x) in curr_locs:
                this_cart = curr_locs[(y,x)]

                this_cart.step()
                curr_locs.pop((y,x))

                if (this_cart.y,this_cart.x) in curr_locs or (this_cart.y,this_cart.x) in new_locs:
                    curr_locs.pop((this_cart.y,this_cart.x), None)
                    new_locs.pop((this_cart.y,this_cart.x), None)

                else:
                    new_locs[(this_cart.y,this_cart.x)]=this_cart
                    
        curr_locs=new_locs                    

A = part_1(inp)
B = part_2(inp)
print('Part A Solution:', str(A[0])+','+str(A[1]))
print('Part B Solution:', str(B[0])+','+str(B[1]))