import math

NCONNECTIONS = 1000

def dist(x,y):
    return sum((a-b)*(a-b) for a,b in zip(x,y))

def find_closest(i, box, boxes, conn=[], circuits=[]):
    d = [[0] for _ in boxes]
    for j, other_box in enumerate(boxes):
#        if i!=j and (j not in conn) and not in_same_circuit(circuits, i, j):
        if i!=j and (j not in conn):
            d[j] = [dist(box, other_box), j]
        else:
            d[j] = [9e99, i]
    d = sorted(d, key=lambda x: x[0])

    return d[0]

def create_circuits(conn):
    circuits = []
    for k, node in enumerate(conn):
        if node==[]:
            continue
        done = False
        myset = set([k]+node)
        for l, circuit in enumerate(circuits):
            circuit_set = set(circuit)
            if myset & circuit_set:
                circuits[l] = list(set(circuit_set|myset))
                done = True
                break
        if not done:
            circuits.append(list(myset))

    return circuits

#def in_same_circuit(circuits, i, j):
#    myset = set([i,j])
#    for circuit in circuits:
#        if (myset & set(circuit))==myset:
#            return True
#    return False

with open('day8_prob1.txt', 'r') as f:
#with open('day8_sample.txt', 'r') as f:
    boxes = [x.split(',') for x in f.read().splitlines()]

# convert all to ints
boxes = [[int(x) for x in y] for y in boxes]

# create array to hold connections
conn = [[] for _ in boxes]

# create array to hold min distances
mdist = [[] for _ in boxes]

# calculate the min distances for each box to other boxes
for i, box in enumerate(boxes):
    mdist[i] = find_closest(i, box, boxes, conn[i]) + [i]

mdist = sorted(mdist, key=lambda x: x[0])
nconn = 0
while nconn < NCONNECTIONS:
    i = mdist[0][2]
    j = mdist[0][1]
#    if mdist[0][1] not in conn[i]:
    conn[i].append(j)
    conn[j].append(i)
    nconn = nconn + 1
    print(str(nconn) + ' connections found')

    circuits = create_circuits(conn)
    # now recalculate the 2 min distances
    mdist[0] = find_closest(i, boxes[i], boxes, conn[i], circuits) + [i]
    mdist[1] = find_closest(j, boxes[j], boxes, conn[j], circuits) + [j]
    # sort
    mdist = sorted(mdist, key=lambda x: x[0])


print(circuits)

cir_lens = [len(x) for x in circuits]
cir_lens.sort(reverse=True)
print()
print(cir_lens)
print()

print(math.prod(cir_lens[0:3]))
