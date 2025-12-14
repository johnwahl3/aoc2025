import math

def area(p1, p2):
    return (abs(p2[1]-p1[1])+1)*(abs(p2[0]-p1[0])+1)

#with open('day9_prob1.txt', 'r') as f:
with open('day9_sample2.txt', 'r') as f:
    spoints = [x.split(',') for x in f.read().splitlines()]

# convert to integers
points = [[int(x[0]), int(x[1])] for x in spoints]

max_size = -1
for i, point1 in enumerate(points):
    for j, point2 in enumerate(points[i+1:]):
        this_area = area(point1, point2)
        if max_size < this_area:
            max_size = this_area
#            print(point1)
#            print(point2)
#            print(max_size)
#            print()

print(max_size)
