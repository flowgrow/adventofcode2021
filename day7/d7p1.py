input = open('input.txt', 'r')
data = list(map(int, input.readline().strip().split(',')))
data.sort()

n = len(data)
median = data[int((n+1)/2)]

print(median)

fuel = 0
for i in data:
    fuel += abs(i-median)

print(fuel)
