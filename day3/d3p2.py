input = open('input.txt', 'r')
firstLine = input.readline().strip()

input.seek(0)
lines = input.readlines()

positions = len(firstLine)

matrix = []


def column(matrix, i):
    return [row[i] for row in matrix]


def countcol(column, countnum=1):
    ones = 0
    zeros = 0
    for i in column:
        if i is 0:
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        return 0 if countnum is 1 else 1
    else:
        return 1 if countnum is 1 else 0

def where(matrix, index, num):
    return [x for x in matrix if x[index] is num]

for i, line in enumerate(lines):
    line = line.strip()
    matrix.append([int(char) for char in line])

params = []

for num in [1,0]:
    m = matrix
    for i in range(0, positions):
        m = where(m, i, countcol(column(m, i), num))
        print(m)
        if (len(m) is 1):
            m = [str(x) for x in m[0]]
            break
    
    params.append(int(''.join(m), 2))
    
print(params, params[0] * params[1])