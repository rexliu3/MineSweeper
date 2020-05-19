from random import randint

mainBoard = []

# 20 - 99 / 18 - 40 / 10 - 10
numRowsColumns = 5
numMines = 10


def print_board(board):
    for i in range(numRowsColumns):
        for j in range(numRowsColumns):
            if j != numRowsColumns - 1:
                print(str(board[i][j]) + "\t", end=" ")
            else:
                print(str(board[i][j]))


def set_up():
    board = []
    for i in range(numRowsColumns):
        board.append([])
        for j in range(numRowsColumns):
            board[i].append(0)
    return board


def place_mines(board):
    for k in range(numMines):
        rowCoordinate = randint(0, numRowsColumns - 1)
        columnCoordinate = randint(0, numRowsColumns - 1)
        while board[rowCoordinate][columnCoordinate] < 0:
            rowCoordinate = randint(0, numRowsColumns - 1)
            columnCoordinate = randint(0, numRowsColumns - 1)
        board[rowCoordinate][columnCoordinate] = -1

        if rowCoordinate != 0 and columnCoordinate != 0:
            if board[rowCoordinate - 1][columnCoordinate - 1] >= 0:
                board[rowCoordinate - 1][columnCoordinate - 1] += 1

        if rowCoordinate != 0:
            if board[rowCoordinate - 1][columnCoordinate] >= 0:
                board[rowCoordinate - 1][columnCoordinate] += 1

        if rowCoordinate != 0 and columnCoordinate != numRowsColumns - 1:
            if board[rowCoordinate - 1][columnCoordinate + 1] >= 0:
                board[rowCoordinate - 1][columnCoordinate + 1] += 1

        if columnCoordinate != 0:
            if board[rowCoordinate][columnCoordinate - 1] >= 0:
                board[rowCoordinate][columnCoordinate - 1] += 1

        if columnCoordinate != numRowsColumns - 1:
            if board[rowCoordinate][columnCoordinate + 1] >= 0:
                board[rowCoordinate][columnCoordinate + 1] += 1

        if rowCoordinate != numRowsColumns - 1 and columnCoordinate != 0:
            if board[rowCoordinate + 1][columnCoordinate - 1] >= 0:
                board[rowCoordinate + 1][columnCoordinate - 1] += 1

        if rowCoordinate != numRowsColumns - 1:
            if board[rowCoordinate + 1][columnCoordinate] >= 0:
                board[rowCoordinate + 1][columnCoordinate] += 1

        if rowCoordinate != numRowsColumns - 1 and columnCoordinate != numRowsColumns - 1:
            if board[rowCoordinate + 1][columnCoordinate + 1] >= 0:
                board[rowCoordinate + 1][columnCoordinate + 1] += 1
    return board


def test_generation(board):
    for test in range(10000):
        for rowCoordinate in range(len(board)):
            for columnCoordinate in range(len(board[0])):
                if board[rowCoordinate][columnCoordinate] >= 0:
                    counter = 0
                    if rowCoordinate != 0 and columnCoordinate != 0:
                        if board[rowCoordinate - 1][columnCoordinate - 1] < 0:
                            counter += 1

                    if rowCoordinate != 0:
                        if board[rowCoordinate - 1][columnCoordinate] < 0:
                            counter += 1

                    if rowCoordinate != 0 and columnCoordinate != numRowsColumns - 1:
                        if board[rowCoordinate - 1][columnCoordinate + 1] < 0:
                            counter += 1

                    if columnCoordinate != 0:
                        if board[rowCoordinate][columnCoordinate - 1] < 0:
                            counter += 1

                    if columnCoordinate != numRowsColumns - 1:
                        if board[rowCoordinate][columnCoordinate + 1] < 0:
                            counter += 1

                    if rowCoordinate != numRowsColumns - 1 and columnCoordinate != 0:
                        if board[rowCoordinate + 1][columnCoordinate - 1] < 0:
                            counter += 1

                    if rowCoordinate != numRowsColumns - 1:
                        if board[rowCoordinate + 1][columnCoordinate] < 0:
                            counter += 1

                    if rowCoordinate != numRowsColumns - 1 and columnCoordinate != numRowsColumns - 1:
                        if board[rowCoordinate + 1][columnCoordinate + 1] < 0:
                            counter += 1
                    if counter != board[rowCoordinate][columnCoordinate]:
                        return False
    return True


mainBoard = set_up()
sub = place_mines(mainBoard)
mainBoard = sub
print_board(mainBoard)
print(test_generation(mainBoard))
