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
min_fuel_usage = 1065186319

for i in range(1, int(max_number)):
    fuel_usage = 0
    for number in numbers:
        if number > i:
            steps = (number - i)
            total_fuel_consumed = int((steps/2) * (1+steps))
            fuel_usage = fuel_usage + total_fuel_consumed
        else:
            steps = (i - number)
            total_fuel_consumed = int((steps/2) * (1+steps))
            fuel_usage = fuel_usage + total_fuel_consumed  

    print("fuel_usage:" + str(fuel_usage))
    print("number:" + str(i))
    if fuel_usage < min_fuel_usage:
        min_fuel_usage = fuel_usage
        

print(min_fuel_usage)