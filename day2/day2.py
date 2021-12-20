"""
advent of code day 2 problemto calculate movement of submarian
"""

f = open('input.txt', 'r')

horizontant_movement = 0
depth_movement = 0

for line in f:
    line = line.replace('\n', '')
    toks = line.split(' ')

    direction = toks[0]
    units = int(toks[1])

    if direction == 'forward':
        horizontant_movement = horizontant_movement + units
    if direction == 'up':
        depth_movement = depth_movement - units
    if direction == 'down':
        depth_movement = depth_movement + units

final_movement = horizontant_movement * depth_movement
print(final_movement)