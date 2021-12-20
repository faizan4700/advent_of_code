"""
most and least commen bits in binary numbers list
"""

def main():
    f = open('input.txt', 'r')
    numbers = []
    numbers2 = []
    for line in f:
        line = line.replace('\n', '')
        numbers.append(line)
        numbers2.append(line)

    oxgen_rating_value = oxgen_rating(numbers)
    co2_rating_value = co2_rating(numbers2)
    print(oxgen_rating_value)
    print(co2_rating_value)
    print(int(oxgen_rating_value,2) * int(co2_rating_value,2))


def oxgen_rating(numbers):

    bit_number = 0

    while len(numbers) > 1:
        print('bit bumber: ' + str(bit_number))
        print(len(numbers))
        relative_counts = 0
        for number in numbers:
            if number[bit_number] == '1':
                relative_counts += 1
            else:
                relative_counts -= 1
        
        bit_to_keep = '1'
        if relative_counts < 0:
            bit_to_keep = '0'

        print('bit to keep: ' + bit_to_keep)
        temp_numbers = [] 
        for number in numbers:
            if number[bit_number] == bit_to_keep:
                temp_numbers.append(number)

        numbers = temp_numbers
        print(len(numbers))
        bit_number += 1
    
    return numbers[0]

def co2_rating(numbers):

    bit_number = 0

    while len(numbers) > 1:
        print('bit bumber: ' + str(bit_number))
        print(len(numbers))
        relative_counts = 0
        for number in numbers:
            if number[bit_number] == '1':
                relative_counts += 1
            else:
                relative_counts -= 1
        
        bit_to_keep = '0'
        if relative_counts < 0:
            bit_to_keep = '1'

        print('bit to keep: ' + bit_to_keep)
        temp_numbers = [] 
        for number in numbers:
            if number[bit_number] == bit_to_keep:
                temp_numbers.append(number)

        numbers = temp_numbers
        print(len(numbers))
        bit_number += 1
    
    return numbers[0]

def toBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

main()