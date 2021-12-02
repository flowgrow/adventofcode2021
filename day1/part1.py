# Python code to
# demonstrate readlines()

# Using readlines()
input = open('input.txt', 'r')
lines = input.readlines()

increase = 0
decrease = 0
equal = 0

prev = None

# Strips the newline character
for line in lines:
    num = int(line)
    if prev is not None:
        if num > prev:
            increase += 1
        elif num < prev:
            decrease += 1
        else:
            equal += 1
    prev = num

print(increase, decrease, equal)