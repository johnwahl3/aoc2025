import math

with open('day6_prob1.txt', 'r') as f:
#with open('day6_sample.txt', 'r') as f:
    math_hw = [x.split() for x in f.read().splitlines()]

math_hw = [list(row) for row in zip(*math_hw)]

tot = 0
for prob in math_hw:
    if prob[-1]=='*':
        ans = math.prod([int(x) for x in prob[:-1]])
    else:
        ans = sum([int(x) for x in prob[:-1]])
    tot = tot + ans
    
print()
print()
print(str(tot) + " summed answers")
