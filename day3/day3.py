"""
most and least commen bits in binary numbers list
"""

def main():
    f = open('input.txt', 'r')

    relative_counts = [0,0,0,0,0,0,0,0,0,0,0,0]

    for line in f:
        line = line.replace('\n', '')
        for i in range(0, len(line)):
            if line[i] == '1':
                relative_counts[i] += 1
            else:
                relative_counts[i] -= 1

    print(relative_counts)
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(0, len(relative_counts)):
        if relative_counts[i] > 0:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    print(gamma_rate)
    print(epsilon_rate)

    power_consumption = int(gamma_rate,2) * int(epsilon_rate,2)

    print(power_consumption)

def toBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

main()