import math
from collections import defaultdict

board = []
commands = []


def draw_line(x1, y1, x2, y2):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    Input coordinates should be integers.
    The result will contain both the start and the end point.
    """

    dx = x2 - x1
    dy = y2 - y1

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        board[y1 + x*xy + y*yy][x1 + x*xx + y*yx] += 1
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy


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

        commands.append([x1, y1, x2, y2])

    board = [[0 for i in range(max_x+1)] for j in range(max_y+1)]


def play_game():
    for command in commands:
        x1 = command[0]
        y1 = command[1]
        x2 = command[2]
        y2 = command[3]

        draw_line(x1, y1, x2, y2)

    # max_count = 0
    # counter = defaultdict(lambda: 0)
    count_two = 0
    for row in board:
        for vent_count in row:
            if vent_count >= 2:
                count_two += 1
            # max_count = max(max_count, vent_count)

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
print_board()
print("result: ", out)
