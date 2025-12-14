import math
from scipy.optimize import differential_evolution, shgo, dual_annealing, direct
import re

def state(lights, buttons, button_presses):
    for i, press in enumerate(button_presses):
        if round(press) %2 == 1:
            for idx in buttons[i]:
                lights[idx] = lights[idx] ^ 1

    return lights

def diff_cost(lights, target):
    light_cost = sum(abs(x-y) for x,y in zip(lights, target))
    return light_cost

def cost_function(x, target, buttons, joltage):
    s0 = [0]*len(target)
    c = 1000*diff_cost(state(s0, buttons, x), target)**2 + abs(sum([round(b) for b in x]))**2
    return c

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
    bounds = [(0,1)]*len(buttons)
    result = differential_evolution(func=cost_function, bounds=bounds, args=(target, buttons, joltage), popsize=100)
#    result = shgo(func=cost_function, bounds=bounds, args=(target, buttons, joltage))
#    result = dual_annealing(func=cost_function, bounds=bounds, args=(target, buttons, joltage))
#    result = direct(func=cost_function, bounds=bounds, args=(target, buttons, joltage))

    this_press = sum(round(x) for x in result.x)
    npress = npress + this_press
    print(npress)
    if result.fun != this_press**2:
        print("Didnt find right minimum:")
        print(this_press)
        print(result.fun)
        print(target)
        print(buttons)
        print(joltage)

print(npress)

