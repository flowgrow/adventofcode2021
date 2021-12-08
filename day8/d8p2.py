import json

input = open('input.txt', 'r')
lines = input.readlines()

possible = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

numbers = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
}


def init_numbers():
    global numbers
    numbers = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }

total = 0
for line in lines:
    line = line.strip()
    riddle, output = line.split(' | ')
    patterns = riddle.split(' ') + output.split(' ')
    output = output.split(' ')

    init_numbers()

    for pattern in patterns:
        characters = set(pattern)

        if len(pattern) == 2:
            if characters not in numbers[1]:
                numbers[1].append(characters)
        elif len(pattern) == 3:
            if characters not in numbers[7]:
                numbers[7].append(characters)
        elif len(pattern) == 4:
            if characters not in numbers[4]:
                numbers[4].append(characters)
        elif len(pattern) == 5:
            if characters not in numbers[2]:
                numbers[2].append(characters)
            if characters not in numbers[3]:
                numbers[3].append(characters)
            if characters not in numbers[5]:
                numbers[5].append(characters)
        elif len(pattern) == 6:
            if characters not in numbers[0]:
                numbers[0].append(characters)
            if characters not in numbers[6]:
                numbers[6].append(characters)
            if characters not in numbers[9]:
                numbers[9].append(characters)
        elif len(pattern) == 7:
            if characters not in numbers[8]:
                numbers[8].append(characters)


    for s in numbers[3]:
        if numbers[1][0].issubset(s):
            numbers[3] = [s]
            numbers[2].remove(s)
            numbers[5].remove(s)
            break


    for s in numbers[9]:
        if numbers[4][0].issubset(s):
            numbers[9] = [s]
            numbers[6].remove(s)
            numbers[0].remove(s)
            break
    

    for s in numbers[0]:
        if numbers[7][0].issubset(s):
            numbers[0] = [s]
            numbers[6].remove(s)
            break
    
    
    if len(numbers[6][0] - numbers[5][0]) == 1:
        numbers[2].remove(numbers[5][0])
        numbers[5].remove(numbers[5][1])
    else:
        numbers[2].remove(numbers[5][1])
        numbers[5].remove(numbers[5][0])

    
    numbers = [
        numbers[0][0],
        numbers[1][0],
        numbers[2][0],
        numbers[3][0],
        numbers[4][0],
        numbers[5][0],
        numbers[6][0],
        numbers[7][0],
        numbers[8][0],
        numbers[9][0]
    ]

    num_str = ''
    for number in output:
        num_set = set(number)
        num_str += str(numbers.index(num_set))
    
    total += int(num_str)
    print(num_str)

print(total)