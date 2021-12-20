"""
finding numbers list in matrices
"""

f = open('input.txt', 'r')

numbers_to_find = []
grid = []
marker_grid = []

for line in f:
    if ',' in line:
        numbers_to_find_str = line.replace('\n', '').split(',')
        for number in numbers_to_find_str:
            numbers_to_find.append(int(number))
    else:
        if len(line) > 1:
            line = line.replace('\n', '')
            toks = line.split(' ')
            row = []
            marker_row = []
            for tok in toks:
                if tok != '':
                    row.append(int(tok))
                    marker_row.append(0)
            
            grid.append(row)
            marker_grid.append(marker_row)
        

print(numbers_to_find)
print(grid)

for drawed_number in numbers_to_find:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == drawed_number:
                marker_grid[i][j] = 1
                row_index = i
                while row_index%5 != 0:
                    row_index -= 1
                    
                if  marker_grid[i][0] == 1 and marker_grid[i][1] == 1 and marker_grid[i][2] == 1 and marker_grid[i][3] == 1 and marker_grid[i][4] == 1:
                    
                    box_sum = 0
                    for k in range(5):
                        for l in range(5):
                            if marker_grid[row_index + k][l] == 0:
                                box_sum = box_sum + grid[row_index + k][l]
                    print(box_sum * drawed_number)
                    exit()
                
                if  marker_grid[row_index][j] == 1 and marker_grid[row_index+1][j] == 1 and marker_grid[row_index+2][j] == 1 and marker_grid[row_index+3][j] == 1 and marker_grid[row_index+4][j] == 1:
                    box_sum = 0
                    for k in range(5):
                        for l in range(5):
                            if marker_grid[row_index + k][l] == 0:
                                box_sum = box_sum + grid[row_index + k][l]
                    print(box_sum * drawed_number)
                    exit()
