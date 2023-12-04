from utils import *

inp = get_input(2023,4)

A = 0
l = len(inp)
cardCt = [int(1) for i in range(l)]

for x in inp:
    ct = 0
    [card, nums] = x.split(': ')
    cardNum = int(card.split()[1])-1
    [winningNums, cardNums] = nums.split(' | ');
    winningNums = [int(t) for t in winningNums.split()]
    cardNums = [int(t) for t in cardNums.split()]
    
    for m in cardNums:
        if m in winningNums:
            ct+=1
    # A
    if ct>0:
        A+=pow(2,ct-1)
    # B
    for i in range(ct):
        cardCt[cardNum+1+i]+=cardCt[cardNum]



print('Part A Solution:', A)
print('Part B Solution:', sum(cardCt))