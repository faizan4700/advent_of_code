"""
advent of code day 2 problemto calculate movement of submarian
"""

f = open('input.txt', 'r')

aim_movement = 0
depth_movement = 0
horizontant_movement = 0

for line in f:
    line = line.replace('\n', '')
    toks = line.split(' ')

    direction = toks[0]
    units = int(toks[1])

    if direction == 'forward':
        horizontant_movement = horizontant_movement + units
        depth_movement = depth_movement + (aim_movement * units) 
    if direction == 'up':
        aim_movement = aim_movement - units
    if direction == 'down':
        aim_movement = aim_movement + units

final_movement = horizontant_movement * depth_movement
print(final_movement)