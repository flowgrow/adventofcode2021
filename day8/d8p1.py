input = open('input.txt', 'r')

lines = input.readlines()

ones = 0
fours = 0
sevens = 0
eights = 0

for line in lines:
    line = line.strip()
    patterns, output = line.split(' | ')
    patterns = patterns.split(' ')
    output = output.split(' ')

    for pattern in output:
        if len(pattern) == 2:
            ones += 1
        elif len(pattern) == 3:
            sevens += 1
        elif len(pattern) == 4:
            fours += 1
        elif len(pattern) == 7:
            eights += 1

total = ones + fours + sevens + eights
print(total, ones, fours, sevens, eights)