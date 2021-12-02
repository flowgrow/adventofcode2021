# Using readlines()
input = open('input.txt', 'r')
lines = input.readlines()

horizontal = 0
depth = 0
aim = 0

for line in lines:
    [command, num] = line.split()
    num = int(num)
    if command == "forward":
        horizontal += num
        depth += num * aim
    elif command == "down":
        aim += num
    elif command == "up":
        aim -= num

print(horizontal, depth, horizontal*depth)
    