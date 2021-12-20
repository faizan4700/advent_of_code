"""
Finding path with lowest risk
"""
import sys

sys.setrecursionlimit(5000)

global final_sum
final_sum = -1
def split(word):
    return [int(char) for char in word]

def split_init(word):
    return [-1 for char in word]

def find_lowest_risk(numbers, i, j, sum, min_paths):
    global final_sum

    proning = False
    if not (i == 0 and j == 0): 
        sum  = sum + numbers[i][j]
        if min_paths[i][j] < 0 or sum <= min_paths[i][j]:
            min_paths[i][j] = sum
        else:
            print('Pronning case')
            proning = True

    if proning is not True:
        if i < (len(numbers) - 1):
            find_lowest_risk(numbers, i+1, j, sum, min_paths)
        if j < len(numbers[0]) -1 :
            find_lowest_risk(numbers, i, j+1, sum, min_paths)

    if i == (len(numbers) - 1) and j == (len(numbers[0]) -1):
        print(min_paths)
        if sum < final_sum or final_sum < 0:
            final_sum = sum

numbers = []
min_paths = []
f = open('input.txt', 'r')
for line in f:
    line = line.replace('\n', '')
    final_row_str = line
    numbers_row = split(line)
    final_row = split(line)
    size = len(numbers_row)
    for i in range(4):
        for j in range(size):
            out_num = (numbers_row[j] + 1)
            if out_num == 10:
                out_num = 1
            final_row.append(out_num)
            final_row_str = final_row_str + str(out_num)
            numbers_row[j] = out_num 
    numbers.append(final_row)
    # print(final_row_str)
    
size = len(numbers)
for i in range(size,size*5):
    row = []
    row_string = ''
    for number in numbers[i - size]:
        out_num = (number + 1)
        if out_num == 10:
            out_num = 1
        row.append(out_num)
        row_string = row_string + (str(out_num))
    numbers.append(row)
    # print(row_string)
        
for i in range(len(numbers)):
    min_paths.append([-1 for number in numbers[i]])
        
# print(min_paths)

find_lowest_risk(numbers, 0, 0, 0, min_paths)
print(final_sum)

# print(min_paths)
