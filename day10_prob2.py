import re
import numpy as np
from scipy.optimize import nnls, minimize, linprog

def cost_func(x, A, b):
    Ax = A@x
    resid = sum([abs(y-z) for y,z in zip(Ax, b)])
    return 10000000*resid*resid + sum(x)

with open('day10_prob1.txt', 'r') as f:
#with open('day10_sample.txt', 'r') as f:
    rows = f.read().splitlines()

targets = []
buttons_set = []
joltages = []
for row in rows:
    matches = re.search(r'\[(.*)\] (.*?) \{(.*)\}', row)
    targets.append(list(matches.group(1).replace('.','0').replace('#','1')))
    targets[-1] = [int(x) for x in targets[-1]]

    buttons_set.append([x[1:-1].split(',') for x in matches.group(2).split(' ')])
    buttons_set[-1] = [[int(x) for x in buttons] for buttons in buttons_set[-1]]

    joltages.append([int(x) for x in matches.group(3).split(',')])

npress = 0

for target, buttons, joltage in zip(targets, buttons_set, joltages):
    # solve A^Tx=B
    A = [[0]*len(joltage) for _ in range(len(buttons))]

    # create the A matrix
    for i, actions in enumerate(buttons):
        for action in actions:
            A[i][action] = 1

    AT = [list(row) for row in zip(*A)]

    AT = np.array(AT)
    b = np.array(joltage)

    bounds = [(0,None)]*len(buttons)
    
#    sol, residuals, rank, s = np.linalg.lstsq(AT, b)
#    result = nnls(A=AT, b=b, maxiter=10000)
#    result = minimize(fun=cost_func, x0=[10]*len(buttons), args=(AT,b), bounds=bounds)
    result = linprog([1]*len(buttons), A_eq=AT, b_eq=b, bounds=bounds, integrality=1)

    n = round(sum(result.x))

    npress += n

print(npress)

