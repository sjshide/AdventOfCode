from collections import defaultdict

f='day14.txt'
arr = []
for x in open(f,"r"):
    arr.append(x)
    

# get rid of newlines:
arr = [x[:-1] for x in arr]


# partially parse equations out
# key is (amt, target) for the product of each reaction
# value is space-separated reagents string
def eqns(arr2):
    d = dict()
    for x in arr2:
        eq = x.split('=>')
        ingredients = eq[0]
        target = eq[1]
        key = tuple(target.split(' ')[1:])
        d[key] = ingredients[:-1]
    return(d)

equations_dict = eqns(arr)

#get the graph structure.
#keys are ingredients (nodes of the graph), and values are lists
#of ingredients in the equation for creating the key
#(so the nodes directly downstream of the key in the DAG)
nodes = defaultdict(list)
for x in equations_dict:
    elt = x[1]
    ingredients = equations_dict[x]
    for input_chem in ingredients.split(', '):
        amt, chem = input_chem.split(' ')
        nodes[elt].append(chem)


# get a topological ordering for this DAG
# unseen is the list of ingredients in any order
# top_order will contain a topological ordering of the nodes

unseen = list(nodes.keys())
top_order = []

while unseen:
    seen_this_round =[]
    for node in unseen:
        check = 0
        # is node downstream of any remaining nodes?
        for y in unseen:
            if node in nodes[y]:
                check=1
        if check ==0:
            top_order.append(node)
            seen_this_round.append(node)
    for node in seen_this_round:
        unseen.remove(node)


# Finally,for a given n, compute how much ore is necessary
# to make n units of fuel
# run through sorted ingredients and calculate how much you need
def orect(n):
    counts = defaultdict(int)

    counts['FUEL'] = n

    for x in top_order:
        for t in equations_dict:
            if t[1]==x:
                thiskey = t
        amt = int(thiskey[0])

        ingredients = equations_dict[thiskey]

        if counts[x]%amt:
            times = (counts[x]//amt) + 1
        else:
            times = counts[x]//amt
        for x in ingredients.split(', '):
            amt2, chem = x.split(' ')
            counts[chem]+=int(amt2)*times

    return(counts['ORE'])


print(orect(1))
