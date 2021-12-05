draws = []
boards = []
markings = []


def find_number(matrix, number):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] is number:
                return (True, r, c)
    return (False, -1, -1)


def find_bingo(marking, board):
    for r, row in enumerate(marking):
        if sum(row) == 5:
            return True

    transposed = list(map(list, zip(*marking)))
    for c, col in enumerate(transposed):
        if sum(col) == 5:
            return True

    return False


def sum_unmarked(marking, board):
    sum = 0
    for r in range(5):
        for c in range(5):
            if marking[r][c] == 0:
                sum += board[r][c]
    return sum


def sum_marked(marking, board):
    sum = 0
    for r in range(5):
        for c in range(5):
            if marking[r][c] == 1:
                sum += board[r][c]
    return sum


def read_data():
    global draws
    global boards
    global markings
    input = open('input.txt', 'r')
    draws = input.readline().strip()
    draws = [int(x) for x in draws.split(',')]

    lines = input.readlines()

    row = 0
    for line in lines:
        line = line.strip()

        if len(line) == 0:
            boards.append([None] * 5)
            markings.append([None] * 5)
            row = 0
        else:
            numbers = [int(x) for x in line.split()]
            boards[-1][row] = numbers
            markings[-1][row] = [0, 0, 0, 0, 0]
            row += 1


def play_game():
    bingos = []
    for i, number in enumerate(draws):
        for j, board in enumerate(boards):
            marking = markings[j]
            found, r, c = find_number(board, number)
            if found:
                marking[r][c] = 1

                if i >= 5:
                    bingo = find_bingo(marking, board)
                    if bingo and board not in bingos:
                        bingos.append(board)
                        if len(bingos) == len(boards):
                            return sum_unmarked(marking, board), number
                        
    return 0, 0


read_data()

sum, number = play_game()

print(sum, number, sum * number)
