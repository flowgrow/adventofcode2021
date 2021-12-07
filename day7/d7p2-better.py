input = open('input.txt', 'r')
data = list(map(int, input.readline().strip().split(',')))
data.sort()

mean = int(round(sum(data)/len(data),0))

fuel = 0
for value in data:
    diff = abs(value - mean)
    fuel += (diff * (diff+1)) / 2

print(fuel)
