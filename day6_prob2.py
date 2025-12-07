import math

with open('day6_prob1.txt', 'r') as f:
#with open('day6_sample.txt', 'r') as f:
    math_hw = f.read().splitlines()

max_l = [-1]*len(math_hw[0].split())
for row in math_hw:
    for i, val in enumerate(row.split()):
        if max_l[i] < len(val):
            max_l[i] = len(val)

pad_hw = []
for row in math_hw:
    pad_row = []
    cur = 0
    for i, l_val in enumerate(max_l):
        pad_row.append(row[cur:cur+l_val])
        cur = cur + l_val + 1
    pad_hw.append(pad_row)

math_hw = [list(row) for row in zip(*pad_hw)]

    

print(math_hw)

correct_hw = []
for prob in math_hw:
#    max_size = -1
#    pad_prob = []
#    for val in prob[:-1]:
#        if len(val) > max_size:
#            max_size = len(val)
#    for val in prob[:-1]:
#        val = ' '*(max_size - len(val)) + val
#        pad_prob.append(val)
#        
#    print(pad_prob)

    l = len(prob) - 1
    new_prob = ['']*l
    for i, val in enumerate(prob[:-1]):
        for i,c in enumerate(val):
            new_prob[l-i-1] = new_prob[l-i-1] + c
            print(new_prob)
    new_prob.append(prob[-1])

    correct_hw.append(new_prob)

print(correct_hw)

tot = 0
for prob in correct_hw:
    fix_prob = []
    for val in prob[:-1]:
        if val:
            fix_prob.append(val)
    fix_prob.append(prob[-1])
    
    if '*' in fix_prob[-1]:
        ans = math.prod([int(x) for x in fix_prob[:-1]])
    else:
        ans = sum([int(x) for x in fix_prob[:-1]])
    tot = tot + ans
    
print()
print()
print(str(tot) + " summed answers")
