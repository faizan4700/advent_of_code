"""
simulating fish growth
"""

f = open('input.txt', 'r')

for line in f:
    fish_lifes_str = line.replace('\n', '').split(',')

ages_hash = [0 for i in range(9)]

for fish_life_str in fish_lifes_str:
    ages_hash[int(fish_life_str)] += 1

print(ages_hash)

for day in range(256):
    print(day)
    
    eight = ages_hash[8]
    seven = ages_hash[7]
    six = ages_hash[6]
    five = ages_hash[5]
    four = ages_hash[4]
    three = ages_hash[3]
    two = ages_hash[2]
    one = ages_hash[1]
    zero = ages_hash[0]

    ages_hash[7] += eight
    ages_hash[6] += seven
    ages_hash[5] += six
    ages_hash[4] += five
    ages_hash[3] += four
    ages_hash[2] += three
    ages_hash[1] += two
    ages_hash[0] += one
    ages_hash[8] += zero
    ages_hash[6] += zero

    ages_hash[8] -= eight
    ages_hash[7] -= seven
    ages_hash[6] -= six
    ages_hash[5] -= five
    ages_hash[4] -= four
    ages_hash[3] -= three
    ages_hash[2] -= two
    ages_hash[1] -= one
    ages_hash[0] -= zero
    print(ages_hash)


sum = 0
for count in ages_hash:
    sum += count

print(sum)