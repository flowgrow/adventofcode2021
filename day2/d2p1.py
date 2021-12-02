# Using readlines()
input = open('input.txt', 'r')
lines = input.readlines()

horizontal = 0
depth = 0

for line in lines:
    [command, num] = line.split()
    num = int(num)
    if command == "forward":
        horizontal += num
    elif command == "down":
        depth += num
    elif command == "up":
        depth -= num

print(horizontal, depth, horizontal*depth)
    