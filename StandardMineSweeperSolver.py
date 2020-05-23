# 0-8 Num of Mines
# 9 Unrevealed
# -5 Selected
# -1 Mine

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
            if board[i][j] != 0 and board[i][j] != 9:
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


def hit_zero(board, rowCoordinate, columnCoordinate):
    rows = len(board)
    columns = len(board[0])
    board[rowCoordinate][columnCoordinate] = 0

    def check_right(board, rowCoordinate, columnCoordinate):
        board[rowCoordinate][columnCoordinate] = 0
        i = 1
        while columnCoordinate + i - 1 != columns - 1 and solvedBoard[rowCoordinate][columnCoordinate + i] == 0:
            check_right(board, rowCoordinate, columnCoordinate + i)
            check_up(board, rowCoordinate, columnCoordinate + i)
            check_down(board, rowCoordinate, columnCoordinate + i)
            # i += 1

    def check_left(board, rowCoordinate, columnCoordinate):
        board[rowCoordinate][columnCoordinate] = 0
        i = 1
        while columnCoordinate - i + 1 != 0 and solvedBoard[rowCoordinate][columnCoordinate - i] == 0:
            check_left(board, rowCoordinate, columnCoordinate - i)
            check_up(board, rowCoordinate, columnCoordinate - i)
            check_down(board, rowCoordinate, columnCoordinate - i)
            # i += 1

    def check_up(board, rowCoordinate, columnCoordinate):
        board[rowCoordinate][columnCoordinate] = 0
        i = 1
        while rowCoordinate + i - 1 != rows - 1 and solvedBoard[rowCoordinate + i][columnCoordinate] == 0:
            check_right(board, rowCoordinate + i, columnCoordinate)
            check_left(board, rowCoordinate + i, columnCoordinate)
            check_up(board, rowCoordinate + i, columnCoordinate)
            # i += 1

    def check_down(board, rowCoordinate, columnCoordinate):
        board[rowCoordinate][columnCoordinate] = 0
        i = 1
        while rowCoordinate - i + 1 != 0 and solvedBoard[rowCoordinate - i][columnCoordinate] == 0:
            check_right(board, rowCoordinate - i, columnCoordinate)
            check_left(board, rowCoordinate - i, columnCoordinate)
            check_down(board, rowCoordinate - i, columnCoordinate)
            # i += 1

    check_right(board, rowCoordinate, columnCoordinate)
    check_left(board, rowCoordinate, columnCoordinate)
    check_down(board, rowCoordinate, columnCoordinate)
    check_up(board, rowCoordinate, columnCoordinate)


def clicked_check(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == -5:
                if solvedBoard[i][j] != -1:
                    board[i][j] = solvedBoard[i][j]
                    if solvedBoard[i][j] == 0:
                        hit_zero(board, i, j)
                else:
                    return False
    return True


def next_edge(board, checked, rowCoordinate, columnCoordinate):
    rows = len(board)
    columns = len(board[0])

    if rowCoordinate != 0:
        if board[rowCoordinate - 1][columnCoordinate] > 0:
            if not checked[rowCoordinate - 1][columnCoordinate]:
                return rowCoordinate - 1, columnCoordinate

    if columnCoordinate != columns - 1:
        if board[rowCoordinate][columnCoordinate + 1] > 0:
            if not checked[rowCoordinate][columnCoordinate + 1]:
                return rowCoordinate, columnCoordinate + 1

    if rowCoordinate != rows - 1:
        if board[rowCoordinate + 1][columnCoordinate] > 0:
            if not checked[rowCoordinate + 1][columnCoordinate]:
                return rowCoordinate + 1, columnCoordinate

    if columnCoordinate != 0:
        if board[rowCoordinate][columnCoordinate - 1] > 0:
            if not checked[rowCoordinate][columnCoordinate - 1]:
                return rowCoordinate, columnCoordinate - 1
    return False


def board_is_solved(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 9:
                return False
    return True


def solve_board(board, checked):
    while not board_is_solved(board):
        row, column = get_first_edge(board)
        if confirm_mine(board, row, column):
            confirmed_mine(board, row, column)
        if confirm_safe(board, row, column):
            confirmed_safe(board, row, column)
        if not clicked_check(board):
            print("wrong")
            return
        checked[row][column] = True
        while next_edge(board, checked, row, column):
            row, column = next_edge(board, checked, row, column)
            if confirm_mine(board, row, column):
                confirmed_mine(board, row, column)
            if confirm_safe(board, row, column):
                confirmed_safe(board, row, column)
            if not clicked_check(board):
                print("wrong")
                return
            checked[row][column] = True
        checked = reset_checked_board(board, checked)
    print("Solved!")


# Main Board already set-up

checkedBoard = set_up_checked_board(mainBoard, checkedBoard)
solve_board(mainBoard, checkedBoard)
print("reached end")

'''print_board(mainBoard)
print(test_generation((solvedBoard)))
print_board(solvedBoard)'''
