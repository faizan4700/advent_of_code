"""
matching 7 segmat display data
"""

final_sum = 0
f = open('input.txt', 'r')
for line in f:
    toks = line.replace('\n', '').split(' | ')
    output_segements_string = toks[1]
    output_segements = output_segements_string.split(' ')
    print(output_segements)
    number = 0
    for i in range(len(output_segements)):
        digit = None
        output_segement = output_segements[i]
        if len(output_segement) == 2:
            digit = 1
        elif len(output_segement) == 4:
            digit = 4
        elif len(output_segement) == 3:
            digit = 7
        elif len(output_segement) == 7:
            digit = 8
        elif len(output_segement) == 5:
            sorted_str = "".join(sorted(output_segement))
            print(sorted_str)
            if sorted_str == 'bcdef':
                digit = 5
            if sorted_str == 'acdfg' or 'acdf' in sorted_str:
                digit = 2
            if sorted_str == 'abcdf':
                digit = 3

        elif len(output_segement) == 6:
            sorted_str = "".join(sorted(output_segement))
            print(sorted_str)
            if sorted_str == 'abcdef':
                digit = 9
            if sorted_str == 'bcdefg':
                digit = 6
            if sorted_str == 'abcdeg':
                digit = 0
        print(digit)

        number = digit * (i+1)

    final_sum = final_sum + number
        
cefdb

g