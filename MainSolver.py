# 0-8 Num of Mines
# 9 Unrevealed
# -5 Selected
# -1 Mine

from MainGenerator import set_up

mainBoard = [
    [0, 0, 0, 1, 9, 9, 9, 9, 9, 9],
    [0, 0, 0, 1, 9, 9, 9, 9, 9, 9],
    [0, 0, 0, 2, 9, 9, 9, 9, 9, 9],
    [1, 1, 0, 1, 9, 9, 9, 9, 9, 9],
    [9, 1, 0, 1, 9, 9, 9, 9, 9, 9],
    [9, 2, 1, 1, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
]

solvedBoard = [
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, -1, 1, 1, -1, 2, 1],
    [0, 0, 0, 2, 3, 3, 2, 1, 2, -1],
    [1, 1, 0, 1, -1, -1, 1, 0, 1, 1],
    [-1, 1, 0, 1, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 0, 0, 1, -1, -1, 1],
    [0, 2, -1, 2, 0, 0, 1, 2, 2, 1],
    [0, 2, -1, 2, 0, 0, 0, 0, 0, 0],
]

checkedBoard = []


def set_up_mainboard_generated():
    board = []
    board = set_up(board, 10, 8, 10)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                hit_zero(board, i, j)
                return board
    return []


def set_up_checked_board(board, checked):
    for i in range(len(board)):
        checked.append([])
        for j in range(len(board[0])):
            if board[i][j] == 0 or board[i][j] == 9 or checking_func(board, i, j):
                checked[i].append(True)
            else:
                checked[i].append(False)
    return checked


def checking_func(board, rowCoordinate, columnCoordinate):
    # Returns False if function is edge
    rows = len(board)
    columns = len(board[0])
    if rowCoordinate != 0 and columnCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate - 1] == 9:
            return False

    if rowCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate] == 9:
            return False

    if rowCoordinate != 0 and columnCoordinate != columns - 1:
        if board[rowCoordinate - 1][columnCoordinate + 1] == 9:
            return False

    if columnCoordinate != 0:
        if board[rowCoordinate][columnCoordinate - 1] == 9:
            return False

    if columnCoordinate != columns - 1:
        if board[rowCoordinate][columnCoordinate + 1] == 9:
            return False

    if rowCoordinate != rows - 1 and columnCoordinate != 0:
        if board[rowCoordinate + 1][columnCoordinate - 1] == 9:
            return False

    if rowCoordinate != rows - 1:
        if board[rowCoordinate + 1][columnCoordinate] == 9:
            return False

    if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
        if board[rowCoordinate + 1][columnCoordinate + 1] == 9:
            return False
    return True


def reset_checked_board(board, checked):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0 or board[i][j] == 9 or checking_func(board, i, j) or board[i][j] == -1:
                checked[i][j] = True
            else:
                checked[i][j] = False
    return checked


def get_first_edge(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            # if board[i][j] != 0 and board[i][j] != 9 and board[i][j] != -1 and not checking_func(board, i, j):
            if board[i][j] != 9 and board[i][j] != -1 and not checking_func(board, i, j):
                return i, j
    return False


def confirm_mine(board, rowCoordinate, columnCoordinate):
    # If the number of open spaces (9) to place mines is less than the number of mines, then there must be mines on all those open spaces
    mineCount = 0
    possibilities = 0
    rows = len(board)
    columns = len(board[0])
    if rowCoordinate != 0 and columnCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate - 1] == 9:
            possibilities += 1
        elif board[rowCoordinate - 1][columnCoordinate - 1] == -1:
            mineCount += 1

    if rowCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate] == 9:
            possibilities += 1
        elif board[rowCoordinate - 1][columnCoordinate] == -1:
            mineCount += 1

    if rowCoordinate != 0 and columnCoordinate != columns - 1:
        if board[rowCoordinate - 1][columnCoordinate + 1] == 9:
            possibilities += 1
        elif board[rowCoordinate - 1][columnCoordinate + 1] == -1:
            mineCount += 1

    if columnCoordinate != 0:
        if board[rowCoordinate][columnCoordinate - 1] == 9:
            possibilities += 1
        elif board[rowCoordinate][columnCoordinate - 1] == -1:
            mineCount += 1

    if columnCoordinate != columns - 1:
        if board[rowCoordinate][columnCoordinate + 1] == 9:
            possibilities += 1
        elif board[rowCoordinate][columnCoordinate + 1] == -1:
            mineCount += 1

    if rowCoordinate != rows - 1 and columnCoordinate != 0:
        if board[rowCoordinate + 1][columnCoordinate - 1] == 9:
            possibilities += 1
        elif board[rowCoordinate + 1][columnCoordinate - 1] == -1:
            mineCount += 1

    if rowCoordinate != rows - 1:
        if board[rowCoordinate + 1][columnCoordinate] == 9:
            possibilities += 1
        elif board[rowCoordinate + 1][columnCoordinate] == -1:
            mineCount += 1

    if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
        if board[rowCoordinate + 1][columnCoordinate + 1] == 9:
            possibilities += 1
        elif board[rowCoordinate + 1][columnCoordinate + 1] == -1:
            mineCount += 1

    return possibilities <= (board[rowCoordinate][columnCoordinate] - mineCount)


def confirmed_mine(board, rowCoordinate, columnCoordinate):
    # All empty spaces (9) are mines
    rows = len(board)
    columns = len(board[0])
    if rowCoordinate != 0 and columnCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate - 1] == 9:
            board[rowCoordinate - 1][columnCoordinate - 1] = -1

    if rowCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate] == 9:
            board[rowCoordinate - 1][columnCoordinate] = -1

    if rowCoordinate != 0 and columnCoordinate != columns - 1:
        if board[rowCoordinate - 1][columnCoordinate + 1] == 9:
            board[rowCoordinate - 1][columnCoordinate + 1] = -1

    if columnCoordinate != 0:
        if board[rowCoordinate][columnCoordinate - 1] == 9:
            board[rowCoordinate][columnCoordinate - 1] = -1

    if columnCoordinate != columns - 1:
        if board[rowCoordinate][columnCoordinate + 1] == 9:
            board[rowCoordinate][columnCoordinate + 1] = -1

    if rowCoordinate != rows - 1 and columnCoordinate != 0:
        if board[rowCoordinate + 1][columnCoordinate - 1] == 9:
            board[rowCoordinate + 1][columnCoordinate - 1] = -1

    if rowCoordinate != rows - 1:
        if board[rowCoordinate + 1][columnCoordinate] == 9:
            board[rowCoordinate + 1][columnCoordinate] = -1

    if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
        if board[rowCoordinate + 1][columnCoordinate + 1] == 9:
            board[rowCoordinate + 1][columnCoordinate + 1] = -1


def confirm_safe(board, rowCoordinate, columnCoordinate):
    # If the number of mines equals the number of of cube, then all other empties (9) are safe
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
    # All empty spaces are safe
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


def hit_zero(board, solvedBoard, rowCoordinate, columnCoordinate):
    rows = len(board)
    columns = len(board[0])
    zeroBoard = []
    # 0 are setup True
    # True means haven't been checked / False means checked
    board[rowCoordinate][columnCoordinate] = 0
    zeroBoard = set_up_checked_board(board, zeroBoard)
    zeroBoard[rowCoordinate][columnCoordinate] = False

    def check_right(board, rowCoordinate, columnCoordinate):
        if columnCoordinate != columns - 1 and solvedBoard[rowCoordinate][
            columnCoordinate + 1] == 0 and zeroBoard[rowCoordinate][columnCoordinate + 1]:
            board[rowCoordinate][columnCoordinate + 1] = 0
            zeroBoard[rowCoordinate][columnCoordinate + 1] = False
            check_right(board, rowCoordinate, columnCoordinate + 1)
            check_up(board, rowCoordinate, columnCoordinate + 1)
            check_down(board, rowCoordinate, columnCoordinate + 1)

    def check_left(board, rowCoordinate, columnCoordinate):
        if columnCoordinate != 0 and solvedBoard[rowCoordinate][columnCoordinate - 1] == 0 and zeroBoard[rowCoordinate][
            columnCoordinate - 1]:
            board[rowCoordinate][columnCoordinate - 1] = 0
            zeroBoard[rowCoordinate][columnCoordinate - 1] = False
            check_left(board, rowCoordinate, columnCoordinate - 1)
            check_up(board, rowCoordinate, columnCoordinate - 1)
            check_down(board, rowCoordinate, columnCoordinate - 1)

    def check_up(board, rowCoordinate, columnCoordinate):
        if rowCoordinate != 0 and solvedBoard[rowCoordinate - 1][columnCoordinate] == 0 and \
                zeroBoard[rowCoordinate - 1][columnCoordinate]:
            board[rowCoordinate - 1][columnCoordinate] = 0
            zeroBoard[rowCoordinate - 1][columnCoordinate] = False
            check_right(board, rowCoordinate - 1, columnCoordinate)
            check_left(board, rowCoordinate - 1, columnCoordinate)
            check_up(board, rowCoordinate + 1, columnCoordinate)

    def check_down(board, rowCoordinate, columnCoordinate):
        if rowCoordinate != rows - 1 and solvedBoard[rowCoordinate + 1][columnCoordinate] == 0 and \
                zeroBoard[rowCoordinate + 1][columnCoordinate]:
            board[rowCoordinate + 1][columnCoordinate] = 0
            zeroBoard[rowCoordinate + 1][columnCoordinate] = False
            check_right(board, rowCoordinate + 1, columnCoordinate)
            check_left(board, rowCoordinate + 1, columnCoordinate)
            check_down(board, rowCoordinate - 1, columnCoordinate)

    check_right(board, rowCoordinate, columnCoordinate)
    check_left(board, rowCoordinate, columnCoordinate)
    check_down(board, rowCoordinate, columnCoordinate)
    check_up(board, rowCoordinate, columnCoordinate)


def clicked_check(board, solvedBoard):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == -5:
                if solvedBoard[i][j] != -1:
                    board[i][j] = solvedBoard[i][j]
                    if solvedBoard[i][j] == 0:
                        hit_zero(board, solvedBoard, j)
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


def board_is_solved(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 9:
                return False
    return True


def solve_board(board, solvedBoard, checked):
    def solver_func(board, checked, row, column):
        if confirm_mine(board, row, column):
            confirmed_mine(board, row, column)
        if confirm_safe(board, row, column):
            confirmed_safe(board, row, column)
        if not clicked_check(board, solvedBoard):
            return
        checked[row][column] = True

    while not board_is_solved(board):
        row, column = get_first_edge(board)
        solver_func(board, checked, row, column)
        while next_edge(board, checked, row, column):
            row, column = next_edge(board, checked, row, column)
            solver_func(board, checked, row, column)
        checked = reset_checked_board(board, checked)
    print("Solved!")

