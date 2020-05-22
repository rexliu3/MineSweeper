mainBoard = [
    [0, 0, 1, 9, 9, 9, 9, 9, 9, 9],
    [0, 0, 1, 9, 9, 9, 9, 9, 9, 9],
    [2, 2, 1, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

solvedBoard = [
    [0, 0, 1, -1, 1, 0, 1, -1, 1, 0],
    [0, 0, 1, 1, 1, 1, 2, 2, 1, 0],
    [2, 2, 1, 0, 0, 1, -1, 1, 0, 0],
    [-1, -1, 1, 1, 1, 2, 1, 1, 0, 0],
    [2, 2, 1, 1, -1, 3, 2, 1, 0, 0],
    [0, 0, 0, 1, 2, -1, -1, 2, 1, 0],
    [1, 1, 0, 0, 1, 2, 3, -1, 1, 0],
    [-1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
]

checkedBoard = []


def set_up_checked_board(board, checked):
    for i in range(len(board)):
        checked.append([])
        for j in range(len(board[0])):
            if board[i][j] == 0 or board[i][j] == 9:
                checked[i].append(True)
            else:
                checked[i].append(False)
    return checked


def reset_checked_board(board, checked):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0 or board[i][j] == 9:
                checked[i] = True
            else:
                checked[i] = False
    return checked


def get_first_edge(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0 and board[i][j] != 9:
                return i, j
    return False


def confirm_mine(board, rowCoordinate, columnCoordinate):
    possibilities = 0
    rows = len(board)
    columns = len(board[0])
    if rowCoordinate != 0 and columnCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate - 1] == 9:
            possibilities += 1

    if rowCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate] == 9:
            possibilities += 1

    if rowCoordinate != 0 and columnCoordinate != columns - 1:
        if board[rowCoordinate - 1][columnCoordinate + 1] == 9:
            possibilities += 1

    if columnCoordinate != 0:
        if board[rowCoordinate][columnCoordinate - 1] == 9:
            possibilities += 1

    if columnCoordinate != columns - 1:
        if board[rowCoordinate][columnCoordinate + 1] == 9:
            possibilities += 1

    if rowCoordinate != rows - 1 and columnCoordinate != 0:
        if board[rowCoordinate + 1][columnCoordinate - 1] == 9:
            possibilities += 1

    if rowCoordinate != rows - 1:
        if board[rowCoordinate + 1][columnCoordinate] == 9:
            possibilities += 1

    if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
        if board[rowCoordinate + 1][columnCoordinate + 1] == 9:
            possibilities += 1

    return possibilities <= board[rowCoordinate][columnCoordinate]


def confirmed_mine(board, rowCoordinate, columnCoordinate):
    rows = len(board)
    columns = len(board[0])
    if rowCoordinate != 0 and columnCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate - 1] < 0:
            board[rowCoordinate - 1][columnCoordinate - 1] = -1

    if rowCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate] < 0:
            board[rowCoordinate - 1][columnCoordinate] = -1

    if rowCoordinate != 0 and columnCoordinate != columns - 1:
        if board[rowCoordinate - 1][columnCoordinate + 1] < 0:
            board[rowCoordinate - 1][columnCoordinate + 1] = -1

    if columnCoordinate != 0:
        if board[rowCoordinate][columnCoordinate - 1] < 0:
            board[rowCoordinate][columnCoordinate - 1] = -1

    if columnCoordinate != columns - 1:
        if board[rowCoordinate][columnCoordinate + 1] < 0:
            board[rowCoordinate][columnCoordinate + 1] = -1

    if rowCoordinate != rows - 1 and columnCoordinate != 0:
        if board[rowCoordinate + 1][columnCoordinate - 1] < 0:
            board[rowCoordinate + 1][columnCoordinate - 1] = -1

    if rowCoordinate != rows - 1:
        if board[rowCoordinate + 1][columnCoordinate] < 0:
            board[rowCoordinate + 1][columnCoordinate] = -1

    if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
        if board[rowCoordinate + 1][columnCoordinate + 1] < 0:
            board[rowCoordinate + 1][columnCoordinate + 1] = -1


def confirm_safe(board, rowCoordinate, columnCoordinate):
    mineCounter = 0
    rows = len(board)
    columns = len(board[0])
    if rowCoordinate != 0 and columnCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate - 1] < 0:
            mineCounter += 1

    if rowCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate] < 0:
            mineCounter += 1

    if rowCoordinate != 0 and columnCoordinate != columns - 1:
        if board[rowCoordinate - 1][columnCoordinate + 1] < 0:
            mineCounter += 1

    if columnCoordinate != 0:
        if board[rowCoordinate][columnCoordinate - 1] < 0:
            mineCounter += 1

    if columnCoordinate != columns - 1:
        if board[rowCoordinate][columnCoordinate + 1] < 0:
            mineCounter += 1

    if rowCoordinate != rows - 1 and columnCoordinate != 0:
        if board[rowCoordinate + 1][columnCoordinate - 1] < 0:
            mineCounter += 1

    if rowCoordinate != rows - 1:
        if board[rowCoordinate + 1][columnCoordinate] < 0:
            mineCounter += 1

    if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
        if board[rowCoordinate + 1][columnCoordinate + 1] < 0:
            mineCounter += 1

    return mineCounter == board[rowCoordinate][columnCoordinate]


def confirmed_safe(board, rowCoordinate, columnCoordinate):
    rows = len(board)
    columns = len(board[0])
    if rowCoordinate != 0 and columnCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate - 1] == 9:
            board[rowCoordinate - 1][columnCoordinate - 1] = -5

    if rowCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate] == 9:
            board[rowCoordinate - 1][columnCoordinate] = -5

    if rowCoordinate != 0 and columnCoordinate != columns - 1:
        if board[rowCoordinate - 1][columnCoordinate + 1] == 9:
            board[rowCoordinate - 1][columnCoordinate + 1] = -5

    if columnCoordinate != 0:
        if board[rowCoordinate][columnCoordinate - 1] == 9:
            board[rowCoordinate][columnCoordinate - 1] = -5

    if columnCoordinate != columns - 1:
        if board[rowCoordinate][columnCoordinate + 1] == 9:
            board[rowCoordinate][columnCoordinate + 1] = -5

    if rowCoordinate != rows - 1 and columnCoordinate != 0:
        if board[rowCoordinate + 1][columnCoordinate - 1] == 9:
            board[rowCoordinate + 1][columnCoordinate - 1] = -5

    if rowCoordinate != rows - 1:
        if board[rowCoordinate + 1][columnCoordinate] == 9:
            board[rowCoordinate + 1][columnCoordinate] = -5

    if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
        if board[rowCoordinate + 1][columnCoordinate + 1] == 9:
            board[rowCoordinate + 1][columnCoordinate + 1] = -5


def clicked_check(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == -5:
                if solved_board[i][j] != -1:
                    board[i][j] = solved_board[i][j]
                else:
                    return False
    return True


def next_edge(board, checked, rowCoordinate, columnCoordinate):
    rows = len(board)
    columns = len(board[0])

    if rowCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate] >= 0:
            if not checked[rowCoordinate - 1][columnCoordinate]:
                return rowCoordinate - 1, columnCoordinate

    if columnCoordinate != columns - 1:
        if board[rowCoordinate][columnCoordinate + 1] >= 0:
            if not checked[rowCoordinate][columnCoordinate + 1]:
                return rowCoordinate, columnCoordinate + 1

    if rowCoordinate != rows - 1:
        if board[rowCoordinate + 1][columnCoordinate] >= 0:
            if not checked[rowCoordinate + 1][columnCoordinate]:
                return rowCoordinate + 1, columnCoordinate

    if columnCoordinate != 0:
        if board[rowCoordinate][columnCoordinate - 1] >= 0:
            if not checked[rowCoordinate][columnCoordinate - 1]:
                return rowCoordinate, columnCoordinate - 1
    return False


def solved_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 9:
                return False
    return True


def solve_board(board, checked):
    row, column = get_first_edge(board)
    if confirm_mine(board, row, column):
        confirmed_mine(board, row, column)
    if confirm_safe(board, row, column):
        confirmed_safe(board, row, column)
    if not clicked_check(board):
        print("wrong")
        return

    while not solved_board(board):
        reset_checked_board(board, checked)
        while not next_edge(board, checked, row, column):
            row, column = next_edge(board, checked, row, column)
            if confirm_mine(board, row, column):
                confirmed_mine(board, row, column)
            if confirm_safe(board, row, column):
                confirmed_safe(board, row, column)
            if not clicked_check(board):
                print("wrong")
                return
    print("Solved!")


# Main Board already set-up

checkedBoard = set_up_checked_board(mainBoard, checkedBoard)
solve_board(mainBoard, checkedBoard)

'''print_board(mainBoard)
print(test_generation((solvedBoard)))
print_board(solvedBoard)'''
