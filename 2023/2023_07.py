from utils import *
from collections import Counter
from functools import cmp_to_key

inp = get_input(2023,7)

hands = []
bids = dict()
for x in inp:
    [hand,bid] = x.split()
    hands.append(hand)
    bids[hand]=int(bid)
    
# inelegant but straightforward  
# Check total counts of cards and use this to get the hand type
# then just output an int in the order of the ranking
# There are much cooler ways of doing this, but went with dumb and easy

def getHandType(hand):
    cts = sorted(list(Counter(hand).values()))
    # high card
    if cts == [1,1,1,1,1]:
        return(1)
    # one pair
    elif cts == [1,1,1,2]:
        return(2)
    # two pair
    elif cts == [1,2,2]:
        return(3)
    # three of a kind
    elif cts == [1,1,3]:
        return(4)
    # full house
    elif cts == [2,3]:
        return(5)
    # four of a kind
    elif cts == [1,4]:
        return(6)
    # five of a kind
    elif cts == [5]:
        return(7)
    return("UNKNOWN HAND TYPE")

cardsA = '23456789TJQKA'
cardsB = 'J23456789TQKA'
cardValsA = dict()
cardValsB = dict()
for i in range(len(cardsA)):
    cardValsA[cardsA[i]]=i
    cardValsB[cardsB[i]]=i

# first hand, second hand, ranking of cards, what J is allowed have subbed
# for A, jSub is just J
# for B, jSub is all cards
def comp(hand1, hand2, cardVals, jSub):
    h1 = str(hand1)
    h2 = str(hand2)
    bestType1 = max([getHandType(h1.replace('J',c)) for c in jSub])
    bestType2 = max([getHandType(h2.replace('J',c)) for c in jSub])
    
    if bestType1!=bestType2:
        return bestType1-bestType2
    else:
        for i in range(5):
            if cardVals[hand1[i]]!=cardVals[hand2[i]]:
                return cardVals[hand1[i]]-cardVals[hand2[i]]
    return(0)

compA = lambda h1,h2: comp(h1,h2,cardValsA,'J')
compB = lambda h1,h2: comp(h1,h2,cardValsB,cardsB)

sortedHandsA = sorted(hands,key=cmp_to_key(compA))
sortedHandsB = sorted(hands,key=cmp_to_key(compB))

A, B = 0, 0

for i in range(len(hands)):
    A+=(i+1)*bids[sortedHandsA[i]]
    B+=(i+1)*bids[sortedHandsB[i]]
    

print('Part A Solution:', A)
print('Part B Solution:', B)