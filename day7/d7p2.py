input = open('input.txt', 'r')
data = list(map(int, input.readline().strip().split(',')))
data.sort()

min_data = min(data)
max_data = max(data)
spread = max_data - min_data

summed_fuel = [0] * spread

for key in data:
    for i in range(min_data, max_data):
        diff = abs(i - key)
        summed_fuel[i] += (diff * (diff+1)) / 2

print(min(summed_fuel), summed_fuel)
