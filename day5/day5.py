"""
intersecting points of lines
"""

f = open('input.txt', 'r')

points_touched = [0 for i in range(1000)]
for i in range(1000):
    points_touched[i] = [0 for i in range(1000)]

for line in f:
    line = line.replace('\n', '').replace(' ', '')
    cooridinates = line.split('->')
    toks = cooridinates[0].split(',')
    x1 = int(toks[0])
    y1 = int(toks[1])
    toks = cooridinates[1].split(',')
    x2 = int(toks[0])
    y2 = int(toks[1])

    

    if x1 == x2:
        print('x1: ' + str(x1))
        print('y1: ' + str(y1))
        print('x2: ' + str(x2))
        print('y2: ' + str(y2))
        if y1 < y2:
            start = y1
            end= y2
        else:
            start = y2
            end= y1

        for i in range(start, end+1):
            points_touched[x1][i] = points_touched[x1][i] + 1
            print(str(x1) + ',' + str(i))

    if y1 == y2:
        print('x1: ' + str(x1))
        print('y1: ' + str(y1))
        print('x2: ' + str(x2))
        print('y2: ' + str(y2))
        if x1 < x2:
            start = x1
            end= x2
        else:
            start = x2
            end= x1

        print(start)
        print(end)

        for i in range(start, end+1):
            points_touched[i][y1] = points_touched[i][y1] + 1
            print(str(i) + ',' + str(y1))

print(points_touched)

danger_points = 0
for i in range(len(points_touched)):
    for j in range(len(points_touched[i])):
        if points_touched[i][j] > 1:
            danger_points += 1

print(danger_points)

