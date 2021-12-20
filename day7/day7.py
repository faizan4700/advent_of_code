"""
match all number
"""

f = open('input.txt', 'r')

numbers = []
max_number = 0
for line in f:
    line = line.replace('\n', '')
    toks = line.split(',')
    for number in toks:
        numbers.append(int(number))
        if int(number) > max_number:
            max_number = int(number)

fuel_usages = []
min_fuel_usage = 1382504

for i in range(1, int(max_number)):
    fuel_usage = 0
    for number in numbers:
        if number > i:
            fuel_usage = fuel_usage + (number - i)
        else:
            fuel_usage = fuel_usage + (i - number)    

    print("fuel_usage:" + str(fuel_usage))
    print("number:" + str(i))
    if fuel_usage < min_fuel_usage:
        min_fuel_usage = fuel_usage
        

print(min_fuel_usage)