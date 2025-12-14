import math
import operator

def area(p1, p2):
    return (abs(p2[1]-p1[1])+1)*(abs(p2[0]-p1[0])+1)

def contained(points, pointi, pointj):
    ncontained = 0
    # check for orientation of left/right and up/down for i,j
    if pointi[0]>pointj[0]:
        oper_x_left = operator.__lt__
        oper_x_right = operator.__gt__
        oper_x_left_on = operator.__le__
        oper_x_right_on = operator.__ge__
    else:
        oper_x_left = operator.__gt__
        oper_x_right = operator.__lt__
        oper_x_left_on = operator.__ge__
        oper_x_right_on = operator.__le__

    if pointi[1]>pointj[1]:
        oper_y_left = operator.__lt__
        oper_y_right = operator.__gt__
        oper_y_left_on = operator.__le__
        oper_y_right_on = operator.__ge__
    else:
        oper_y_left = operator.__gt__
        oper_y_right = operator.__lt__
        oper_y_left_on = operator.__ge__
        oper_y_right_on = operator.__le__

    for k, point in enumerate(points):
        if i==k or j==k:
            continue

        print()
        print(point)
        print(pointi)
        print(pointj)
        # check if any point is contained, if so cant be a good rectangle
        if oper_x_left(point[0], pointi[0]) and \
           oper_x_right(point[0], pointj[0]) and \
           oper_y_left(point[1], pointi[1]) and \
           oper_y_right(point[1], pointj[1]):
            return True

        # check for even number on the lines of the rectangle
        if oper_x_left_on(point[0], pointi[0]) and \
           oper_x_right_on(point[0], pointj[0]) and \
           (point[1]==pointi[1] or point[1]==pointj[1]):
            ncontained = ncontained + 1

        if oper_y_left_on(point[1], pointi[1]) and \
           oper_y_right_on(point[1], pointj[1]) and \
           (point[0]==pointi[0] or point[0]==pointj[0]):
            ncontained = ncontained + 1

    print(ncontained)
    if (ncontained%2)==1:
        return True
    else:
        return False

def between(x, x1, x2):
    if x1>x2:
        return x>x2 and x<x1
    else:
        return x<x2 and x>x1

def between_or_eq(x, x1, x2):
    if x1>x2:
        return x>=x2 and x<=x1
    else:
        return x<=x2 and x>=x1

def cross_polygon(points, p1, p2):
    # possible but unlikely for this problem, leads to another whole chain of checks
    if p2[0]==p1[0]:
        return True
    if p2[1]==p1[1]:
        return True
    m = (p2[1]-p1[1]) / (p2[0]-p1[0])
    b = p1[1] - m*p1[0]

#    print('ref line:')
#    print(p1)
#    print(p2)
#    print(m)
#    print(b)
#    print()
    for i, line_start in enumerate(points):
        if i == len(points)-1:
            line_end = points[0]
        else:
            line_end = points[i+1]

        if line_start==p1 or line_start==p2 or line_end==p1 or line_end==p2:
            continue

            
#        print('checking:')
#        print(line_start)
#        print(line_end)
        # vertical line
        if line_start[0]==line_end[0] and \
           between(line_start[0], p1[0], p2[0]):
            y = m*line_start[0] + b
#            print(y)
            if between_or_eq(y, line_start[1], line_end[1]):
#                print('failed vertical')
                return True
        # horizontal line
        elif line_start[1]==line_end[1] and \
             between(line_start[1], p1[1], p2[1]):
            x = (line_start[1]-b) / m
#            print(x)
            if between_or_eq(x, line_start[0], line_end[0]):
#                print('failed horizontal')
                return True
    return False

#with open('day9_prob1.txt', 'r') as f:
with open('day9_sample3.txt', 'r') as f:
    spoints = [x.split(',') for x in f.read().splitlines()]

# convert to integers
points = [[int(x[0]), int(x[1])] for x in spoints]




























max_size = 0
for i, point1 in enumerate(points):
    for j, point2 in enumerate(points[i+1:]):
        this_area = area(point1, point2)
        if max_size < this_area:
#            print('area is:')
#            print(this_area)
            # check that all other points not contained
            if not (cross_polygon(points, point1, point2) or \
                    cross_polygon(points, [point1[0],point2[1]], [point2[0],point1[1]])):
#            if not (cross_polygon(points, point1, [point1[0], point2[1]]) or \
#                    cross_polygon(points, [point1[0], point2[1]], point2) or \
#                    cross_polygon(points, point2, [point2[0], point1[1]]) or \
#                    cross_polygon(points, [point2[0], point1[1]], point1)):
                max_size = this_area
                max_points = [points[i], points[j+i+1]]
#                print('================NEW MAX================')
#                print(max_size)

#            if not contained(points, points[i], points[j+i+1]): 
#                max_size = this_area
#                max_points = [points[i], points[j+i+1]]
#            print(point1)
#            print(point2)
#            print(max_size)
#            print()


print(max_size)
print(max_points)
