import numpy as np

def near_tot(layout, i, j):
    xmin = max(0, i-1)
    ymin = max(0, j-1)
    xmax = min(len(layout)-1, i+1)
    ymax = min(len(layout[0])-1, j+1)

    tot = -1
    for k in range(xmin,xmax+1):
        for l in range(ymin,ymax+1):
            tot = tot + layout[k][l]
                
    return tot
    
def remove_max(layout, tot):
    can_move = 0
    id = np.ones((len(layout),len(layout[0])))
    for i, row in enumerate(layout):
        for j, spot in enumerate(row):
            if spot and (near_tot(layout, i, j)<4):
                can_move = can_move + 1
                id[i][j] = 0

    layout = layout * id
    tot = tot + can_move
#    print(can_move)
#    print(layout)
    if can_move:
        tot = remove_max(layout, tot)

    return tot


with open('day4_prob1.txt', 'r') as f:
#with open('day4_sample.txt', 'r') as f:
    slayout = [list(row) for row in f.read().replace('.','0').replace('@','1').splitlines()]

layout = np.array([[int(x) for x in row] for row in slayout])
n_moved = 0

n_moved = remove_max(layout, n_moved)

  
print()
print()
print(str(n_moved) + " packages can be moved")
