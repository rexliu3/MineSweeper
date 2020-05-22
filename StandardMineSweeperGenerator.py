from random import randint

mainBoard = []

# 20 - 99 / 18 - 40 / 10 - 10
numRows = 10
numColumns = 10
numMines = 10


def print_board(board):
    columns = len(board[0])
    rows = len(board)
    for i in range(rows):
        for j in range(columns):
            if j != columns - 1:
                print(str(board[i][j]) + "\t", end=" ")
            else:
                print(str(board[i][j]))


def place_mines(board, mines):
    columns = len(board[0])
    rows = len(board)
    for k in range(mines):
        rowCoordinate = randint(0, rows - 1)
        columnCoordinate = randint(0, columns - 1)
        while board[rowCoordinate][columnCoordinate] < 0:
            rowCoordinate = randint(0, rows - 1)
            columnCoordinate = randint(0, columns - 1)
        board[rowCoordinate][columnCoordinate] = -1

        if rowCoordinate != 0 and columnCoordinate != 0:
            if board[rowCoordinate - 1][columnCoordinate - 1] >= 0:
                board[rowCoordinate - 1][columnCoordinate - 1] += 1

        if rowCoordinate != 0:
            if board[rowCoordinate - 1][columnCoordinate] >= 0:
                board[rowCoordinate - 1][columnCoordinate] += 1

        if rowCoordinate != 0 and columnCoordinate != columns - 1:
            if board[rowCoordinate - 1][columnCoordinate + 1] >= 0:
                board[rowCoordinate - 1][columnCoordinate + 1] += 1

        if columnCoordinate != 0:
            if board[rowCoordinate][columnCoordinate - 1] >= 0:
                board[rowCoordinate][columnCoordinate - 1] += 1

        if columnCoordinate != columns - 1:
            if board[rowCoordinate][columnCoordinate + 1] >= 0:
                board[rowCoordinate][columnCoordinate + 1] += 1

        if rowCoordinate != rows - 1 and columnCoordinate != 0:
            if board[rowCoordinate + 1][columnCoordinate - 1] >= 0:
                board[rowCoordinate + 1][columnCoordinate - 1] += 1

        if rowCoordinate != rows - 1:
            if board[rowCoordinate + 1][columnCoordinate] >= 0:
                board[rowCoordinate + 1][columnCoordinate] += 1

        if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
            if board[rowCoordinate + 1][columnCoordinate + 1] >= 0:
                board[rowCoordinate + 1][columnCoordinate + 1] += 1
    return board


def set_up(board, rows, columns, mines):
    for i in range(rows):
        board.append([])
        for j in range(columns):
            board[i].append(0)
    board = place_mines(board, mines)
    return board


def test_generation(board):
    columns = len(board[0])
    rows = len(board)
    for test in range(10000):
        for rowCoordinate in range(rows):
            for columnCoordinate in range(columns):
                if board[rowCoordinate][columnCoordinate] >= 0:
                    counter = 0
                    if rowCoordinate != 0 and columnCoordinate != 0:
                        if board[rowCoordinate - 1][columnCoordinate - 1] < 0:
                            counter += 1

                    if rowCoordinate != 0:
                        if board[rowCoordinate - 1][columnCoordinate] < 0:
                            counter += 1

                    if rowCoordinate != 0 and columnCoordinate != columns - 1:
                        if board[rowCoordinate - 1][columnCoordinate + 1] < 0:
                            counter += 1

                    if columnCoordinate != 0:
                        if board[rowCoordinate][columnCoordinate - 1] < 0:
                            counter += 1

                    if columnCoordinate != columns - 1:
                        if board[rowCoordinate][columnCoordinate + 1] < 0:
                            counter += 1

                    if rowCoordinate != rows - 1 and columnCoordinate != 0:
                        if board[rowCoordinate + 1][columnCoordinate - 1] < 0:
                            counter += 1

                    if rowCoordinate != rows - 1:
                        if board[rowCoordinate + 1][columnCoordinate] < 0:
                            counter += 1

                    if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
                        if board[rowCoordinate + 1][columnCoordinate + 1] < 0:
                            counter += 1
                    if counter != board[rowCoordinate][columnCoordinate]:
                        return False
    return True


mainBoard = set_up(mainBoard, numRows, numColumns, numMines)
# print_board(mainBoard)
# print(test_generation(mainBoard))
