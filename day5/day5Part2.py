"""
intersecting points of lines
"""

f = open('input.txt', 'r')

grid_size = 1000

points_touched = [0 for i in range(grid_size)]
for i in range(grid_size):
    points_touched[i] = [0 for i in range(grid_size)]

max_x = 0
max_y = 0

for line in f:
    line = line.replace('\n', '').replace(' ', '')
    cooridinates = line.split('->')
    toks = cooridinates[0].split(',')
    x1 = int(toks[0])
    y1 = int(toks[1])
    toks = cooridinates[1].split(',')
    x2 = int(toks[0])
    y2 = int(toks[1])

    if x1 > max_x:
        max_x = x1
    if y1 > max_y:
        max_y = y1

    if x2 > max_x:
        max_x = x2
    if y2 > max_y:
        max_y = y2

    if x1 == x2:
        if y1 < y2:
            start = y1
            end= y2
        else:
            start = y2
            end= y1

        for i in range(start, end+1):
            points_touched[x1][i] = points_touched[x1][i] + 1
            # print(str(x1) + ',' + str(i))

    elif y1 == y2:
        if x1 < x2:
            start = x1
            end= x2
        else:
            start = x2
            end= x1

        

        for i in range(start, end+1):
            points_touched[i][y1] = points_touched[i][y1] + 1
            # print(str(i) + ',' + str(y1))

    else:
        # slope
        m = (y2-y1)/(x2-x1)

        if int(m) == 1 or int(m) == -1:
            print('x1: ' + str(x1))
            print('y1: ' + str(y1))
            print('x2: ' + str(x2))
            print('y2: ' + str(y2))
            if x1 < x2:
                x_min = x1
                x_max = x2
            else:
                x_min = x2
                x_max = x1

            if y1 < y2:
                y_min = y1
                y_max = y2
            else:
                y_min = y2
                y_max = y1

            if x1 > x2 and y1 < y2:
                for i in range(max(x1-x2, y2 - y1) + 1):
                    points_touched[x1 - i][y1 + i] = points_touched[x1 - i][y1 + i] + 1

            if x1 < x2 and y1 > y2:
                for i in range(max(x2-x1, y1 - y2) + 1):
                    points_touched[x1 + i][y1 - i] = points_touched[x1 + i][y1 - i] + 1
  
            if x1 < x2 and y1 < y2:
                for i in range(x_max - x_min + 1):
                    points_touched[x1 + i][y1 + i] = points_touched[x1 + i][y1 + i] + 1
  
            if x1 > x2 and y1 > y2:
                for i in range(x_max - x_min + 1):
                    points_touched[x1 - i][y1 - i] = points_touched[x1 - i][y1 - i] + 1

danger_points = 0
for i in range(len(points_touched)):
    for j in range(len(points_touched[i])):
        if points_touched[i][j] > 1:
            danger_points += 1

print(danger_points)

