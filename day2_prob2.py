def count_invalid(x):
    sx = str(x)
    n = len(sx)
    max_digits = int(n/2)
    dupe = False
    for i in range(1,max_digits+1):
        for j in range(0,n-i,i):
            if int(sx[j]) == 0:
                continue
            dupe = sx[j]==sx[j+i]
            if dupe:
                print(x)
                return dupe
    return dupe

def find_rep_dupe(x):
    sx = str(x)
    n = len(sx)
    max_digits = int(n/2)
    for i in range(1,max_digits+1):
        dupe = True
        for j in range(0,n-i,i):
            dupe = dupe and (sx[j:j+i]==sx[j+i:j+i+i])
        if dupe:
            return True
    return False

def find_dupe(x):
    sx = str(x)
    n = len(sx)
    if n % 2:
        return False
    else:
        i = int(n/2)
        return sx[:i]==sx[i:]

with open('day2_prob2.txt', 'r') as f:
#with open('day2_sample.txt', 'r') as f:
    bounds = [x.split('-') for x in f.read().split(',')]

invalid = 0
for bound in bounds:
    for x in range(int(bound[0]), int(bound[1])+1):
        invalid = invalid + (x if find_rep_dupe(x) else 0)

print()
print()
print(str(invalid) + " summed total")
