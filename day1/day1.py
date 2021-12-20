"""
calculate the number of times the measurement increased
"""

f = open('input.txt', 'r')
values = []
for line in f:
    line = line.replace('\n', '')
    value = int(line)
    values.append(value)

print(len(values))
increase_count = 0
for i in range(1,len(values)):
    if values[i] > values[i-1]:
        increase_count = increase_count + 1

print(increase_count)