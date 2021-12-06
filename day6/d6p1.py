input = open('input.txt', 'r')
state = list(map(int, input.readline().split(',')))
count = len(state)

for i in range(80):
    print(i)
    for j in range(count):
        state[j] -= 1
        if state[j] == -1:
            state[j] = 6
            state.append(8)
            count += 1

print(state)
print(count)