from random import randint

board = []

# 20 - 99 / 18 - 40 / 10 - 10
numRowsColumns = 20
numMines = 99


def print_board():
    for i in range(numRowsColumns):
        for j in range(numRowsColumns):
            if j != numRowsColumns - 1:
                print(str(board[i][j]) + "\t", end=" ")
            else:
                print(str(board[i][j]))


def set_up():
    for i in range(numRowsColumns):
        board.append([])
        for j in range(numRowsColumns):
            board[i].append(0)


def place_mines():
    for k in range(numMines):
        rowCoordinate = randint(0, numRowsColumns - 1)
        columnCoordinate = randint(0, numRowsColumns - 1)
        while board[rowCoordinate][columnCoordinate] < 0:
            rowCoordinate = randint(0, numRowsColumns - 1)
            columnCoordinate = randint(0, numRowsColumns - 1)
        board[rowCoordinate][columnCoordinate] = -1

        try:
            if board[rowCoordinate - 1][columnCoordinate - 1] >= 0:
                board[rowCoordinate - 1][columnCoordinate - 1] += 1
        except IndexError:
            pass
        try:
            if board[rowCoordinate - 1][columnCoordinate] >= 0:
                board[rowCoordinate - 1][columnCoordinate] += 1
        except IndexError:
            pass
        try:
            if board[rowCoordinate - 1][columnCoordinate + 1] >= 0:
                board[rowCoordinate - 1][columnCoordinate + 1] += 1
        except IndexError:
            pass
        try:
            if board[rowCoordinate][columnCoordinate - 1] >= 0:
                board[rowCoordinate][columnCoordinate - 1] += 1
        except IndexError:
            pass
        try:
            if board[rowCoordinate][columnCoordinate + 1] >= 0:
                board[rowCoordinate][columnCoordinate + 1] += 1
        except IndexError:
            pass
        try:
            if board[rowCoordinate + 1][columnCoordinate - 1] >= 0:
                board[rowCoordinate + 1][columnCoordinate - 1] += 1
        except IndexError:
            pass
        try:
            if board[rowCoordinate + 1][columnCoordinate] >= 0:
                board[rowCoordinate + 1][columnCoordinate] += 1
        except IndexError:
            pass
        try:
            if board[rowCoordinate + 1][columnCoordinate + 1] >= 0:
                board[rowCoordinate + 1][columnCoordinate + 1] += 1
        except IndexError:
            pass


set_up()
place_mines()
print_board()
