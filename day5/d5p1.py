import math
from collections import defaultdict

board = []
commands = []


def draw_line(x1, y1, x2, y2):
    dX = abs(x2-x1)
    dY = abs(y2-y1)
    if dX > dY:
        y_step = dY / dX
        for i, x in enumerate(range(x1, x2+1)):
            y = math.floor(y1 + i * y_step)
            board[y][x] += 1
    else:
        x_step = dX / dY
        for i, y in enumerate(range(y1, y2+1)):
            x = math.floor(x1 + i * x_step)
            board[y][x] += 1
    
def read_data():
    global board
    input = open('input.txt', 'r')
    lines = input.readlines()

    max_x = 0
    max_y = 0
    for line in lines:
        line = line.strip()
        p1, p2 = line.split(' -> ')
        x1, y1 = map(int, p1.split(','))
        x2, y2 = map(int, p2.split(','))

        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)

        commands.append([min(x1, x2), min(y1,y2) , max(x1, x2), max(y1,y2)])

    board = [[0 for i in range(max_x+1)] for j in range(max_y+1)]
    

def play_game():
    for command in commands:
        x1 = command[0]
        y1 = command[1]
        x2 = command[2]
        y2 = command[3]
        if x1 == x2 or y1 == y2:
            draw_line(x1, y1, x2, y2)

    #max_count = 0
    #counter = defaultdict(lambda: 0)
    count_two = 0
    for row in board:
        for vent_count in row:
            if vent_count >= 2:
                count_two += 1
            #max_count = max(max_count, vent_count)

    return count_two

def to_str(x):
    if x == 0:
        return '.'
    else:
        return str(x)

def print_board():
    for row in board:
        print(''.join(map(to_str, row)))


read_data()
out = play_game()
#print_board()
print("result: ", out)
