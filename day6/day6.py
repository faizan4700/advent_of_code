"""
simulating fish growth
"""

f = open('input.txt', 'r')

for line in f:
    fish_lifes_str = line.replace('\n', '').split(',')

fish_lifes = []
for i in range(len(fish_lifes_str)):
    fish_lifes.append(int(fish_lifes_str[i]))

for day in range(256):
    print(day)
    size = len(fish_lifes)
    for i in range(size):
        if fish_lifes[i] == 0:
            fish_lifes[i] = 6
            fish_lifes.append(8)
        else:
            fish_lifes[i] -= 1

print(fish_lifes)
print(len(fish_lifes))
