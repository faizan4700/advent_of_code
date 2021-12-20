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
for i in range(0,len(values)-3):
    window1_sum = values[i] + values[i + 1] + values[i + 2]
    window2_sum = values[i+1] + values[i + 2] + values[i + 3]
    if window2_sum > window1_sum:
        increase_count = increase_count + 1

print(increase_count)