# Using readlines()
input = open('input.txt', 'r')
lines = input.readlines()

positions = []

for i, line in enumerate(lines):
    line = line.strip()
    
    if i is 0:
        positions = [0] * len(line)
    
    for j, num in enumerate(line):
        num = int(num)
        if num is 1:
            positions[j] += 1
        else:
            positions[j] -= 1

gamma = ''
epsilon = ''

for p in positions:
    if p > 0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma, epsilon, gamma*epsilon)
