from shapely import Polygon, overlaps
from shapely.geometry import box

def area(p1, p2):
    return (abs(p2[1]-p1[1])+1)*(abs(p2[0]-p1[0])+1)

with open('day9_prob1.txt', 'r') as f:
#with open('day9_sample3.txt', 'r') as f:
    spoints = [x.split(',') for x in f.read().splitlines()]

# convert to integers
points = [[int(x[0]), int(x[1])] for x in spoints]

polygon = Polygon(points)

max_size = 0
for i, point1 in enumerate(points[:-1]):
    for j, point2 in enumerate(points[i+1:]):
        if area(point1, point2)>max_size:
            new_polygon = box(point1[0],point1[1], point2[0], point2[1])
            if overlaps(polygon, new_polygon):
                continue
            else:
                max_size = area(point1, point2)
                max_points = [point1, point2]

    
print(max_size)
print(max_points)

























