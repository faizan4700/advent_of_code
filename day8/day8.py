"""
matching 7 segmat display data
"""

count = 0
f = open('input2.txt', 'r')
for line in f:
    toks = line.replace('\n', '').split(' | ')
    output_segements_string = toks[1]
    output_segements = output_segements_string.split(' ')
    print(output_segements)
    for output_segement in output_segements:
        if len(output_segement) == 2 or len(output_segement) == 4 or len(output_segement) == 3 or len(output_segement) == 7:
            count += 1

print(count)