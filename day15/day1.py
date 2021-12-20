"""
Finding path with lowest risk
"""

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
            proning = True

    if proning is not True:
        if i < (len(numbers) - 1):
            find_lowest_risk(numbers, i+1, j, sum, min_paths)
        if j < len(numbers[0]) -1 :
            find_lowest_risk(numbers, i, j+1, sum, min_paths)

    if i == (len(numbers) - 1) and j == (len(numbers[0]) -1):
        # print(sum)
        if sum < final_sum or final_sum < 0:
            final_sum = sum

numbers = []
min_paths = []
f = open('input.txt', 'r')
for line in f:
    line = line.replace('\n', '')
    numbers.append(split(line))
    min_paths.append(split_init(line))
    
print(min_paths)

find_lowest_risk(numbers, 0, 0, 0, min_paths)
print(final_sum)

print(min_paths)
