# Python code to
# demonstrate readlines()

# Using readlines()
input = open('input.txt', 'r')
lines = input.readlines()

increase = 0
decrease = 0
equal = 0

sums = []

# Strips the newline character
for i, line in enumerate(lines):
    num = int(line)
    sums.append(num)

    if i >= 1:
        sums[i-1] += num
    if i >= 2:
        sums[i-2] += num

print(sums)    
prev = None

# Strips the newline character
for sum in sums:
    if prev is not None:
        if sum > prev:
            increase += 1
        elif sum < prev:
            decrease += 1
        else:
            equal += 1
    prev = sum


print(increase, decrease, equal)
