from utils import *

inp = get_input(2021,4)

## Very hacky, probably should've made a class like a good swe would.
## Also I was counting diagonals as wins and somehow passed both tests...
## Very lucky on that one. Fixed here.


new_inp = []
for x in inp:
    if x and x[0]==' ':
        x=x[1:]
    new_inp.append(x.replace('  ',' '))

    
winners = []
for i in range(5):
    row, col = [], []
    for j in range(5):
        row.append((i,j))
        col.append((j,i))    
    winners.append(set(row))
    winners.append(set(col))
    


def winner(s):
    # check if 'seen squares' contains a winner
    global winners
    for x in winners:
        if x<=s:
            return(1)
    return(0)



reads = inp[0]


# boards is a list of dicts with key = positions with the value = value they contain for each board
# rev_boards is just this with key and value reversed
# assumes that boards have no repeat entries, but this seems ok

boards = []
rev_boards = []

for i in range(2,len(new_inp),6):
    rows = new_inp[i:i+5]
    
    this_board = dict()
    this_rev_board = dict()
    
    for i in range(5):
        for j in range(5):
            this_board[(i,j)] = rows[i].split(' ')[j]
            this_rev_board[this_board[(i,j)]] = (i,j)
            
    boards.append(this_board)
    rev_boards.append(this_rev_board)

# list of sets of what squares have been read out for each board
seen = []
for x in boards:
    seen.append(set([]))    

# A
# Run through 'reads' and stop when there's a winning board
# when stops, i will be the winning board index, and x will be the last number read
for x in reads.split(','):
    check=0
    for i in range(len(rev_boards)):
        board = rev_boards[i]
    
        if x in board:
            seen[i].add(board[x])
        if winner(seen[i]):
            check=1
            break
    if check==1:
        break    
    
ct =0
for square in boards[i]:
    if square not in seen[i]:
        ct+=int(boards[i][square])
A = ct*int(x)
    
    
# B
# Just run through it all, and keep track of the last one that finished

seen = []
for x in boards:
    seen.append(set([]))
    
won = set([]) # boards that have won
last_won = -1  # index of last winning board
last_won_read = -1 # number that was read when the last guy won
win_state = -1 # state of the board when it won

for x in reads.split(','):
    for i in range(len(rev_boards)):
        board = rev_boards[i]
    
        if x in board:
            seen[i].add(board[x])
            
        if winner(seen[i]):
            if i not in won:
                last_won = i
                last_won_read = x
                win_state = set(list(seen[i]))
                
                won.add(i)
                
ct =0
for x in boards[last_won]:
    if x not in win_state:
        ct+=int(boards[last_won][x])

        
B = ct*int(last_won_read)    
    
print('Part A Solution:', A)
print('Part B Solution:', B)