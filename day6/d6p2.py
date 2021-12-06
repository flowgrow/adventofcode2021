import json

input = open('input.txt', 'r')
data = list(map(int, input.readline().split(',')))
state = {
    -1: 0,
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}


def sum_up():
    sum = 0
    for key in state:
        sum += state[key]
    return sum


def create_state():
    for x in data:
        state[x] += 1


create_state()

for i in range(256):
    
    for j in range(-1, 8):
        state[j] = state[j+1]
    state[8] = 0

    if state[-1] > 0:
        state[6] += state[-1]
        state[8] = state[-1]
        state[-1] = 0


print(sum_up())