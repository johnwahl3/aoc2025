import re

with open('day12_prob1.txt', 'r') as f:
#with open('day12_sample.txt', 'r') as f:
    shapes = f.read().split('\n\n')

tiles = []
nfilled = []

for shape in shapes[:-1]:
    tiles.append(shape.split(':')[1].strip())
    nfilled.append(len(re.findall('#', tiles[-1])))

print(tiles)
print(nfilled)

regions = []
for region in shapes[-1].splitlines():
    x = [y.strip() for y in region.split(':')]
    nshapes = [int(y) for y in x[1].split(' ')]
    size = [int(y) for y in x[0].split('x')]
    regions.append([size[0], size[1], nshapes])

print(regions)
    
fit = [True] * len(regions)

# check if the number of # is too large
for i, region in enumerate(regions):
    n_req = sum([x*y for x,y in zip(nfilled, region[2])])
    if n_req>region[0]*region[1]:
        fit[i] = False


# now see if we can simply lay down the tiles side by side to fit
fit_simple = [x for x in fit]
for i, region in enumerate(regions):
    n_fit = int(region[0]/3)*int(region[1]/3)
    if n_fit>region[0]*region[1]:
        fit_simple = False


print(len(regions))
print()
print(fit)
print(sum(fit))
print()
print(fit_simple)
print(sum(fit_simple))
