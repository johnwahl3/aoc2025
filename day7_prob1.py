import math

def propagate_tachyons(grid, t, nsplit, row):
    new_tachyons = []
#    for x in t:
#        print(x)
#    print(row)
    for i,x in enumerate(zip(grid[row-1], t[row-1])):
        if x[0]=='^':
            new_tachyons.append(0)
            if x[1]>0:
                nsplit = nsplit + 1
                if i>0:
                    new_tachyons[i-1] = new_tachyons[i-1] + x[1]
                if i<len(grid[0])-1:
                    new_tachyons.append(x[1])
        else:
            if len(new_tachyons)<=i:
                new_tachyons.append(0)
            if x[1]>0:
                new_tachyons[i] = new_tachyons[i] + x[1]
                
    t.append(new_tachyons)
    row = row + 1

    if row < len(grid):
        t, nsplit, row = propagate_tachyons(grid, t, nsplit, row)

    return t, nsplit, row

with open('day7_prob1.txt', 'r') as f:
#with open('day7_sample.txt', 'r') as f:
    tachyon_grid = [list(x) for x in f.read().splitlines()]

tachyons = [[0 if x!='S' else 1 for x in tachyon_grid[0]]]

nsplit = 0
nworlds = 1
row = 1

tachyons, nsplit, row = propagate_tachyons(tachyon_grid, tachyons, nsplit, row)

for row in tachyons:
    print(row)
for row in tachyon_grid:
    print(''.join(row))
print(nsplit)
print(sum(tachyons[-1]))
