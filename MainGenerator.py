from random import randint


def print_board(board, numRowsColumns, numMines):
    for i in range(numRowsColumns):
        for j in range(numRowsColumns):
            if j != numRowsColumns - 1:
                print(str(board[i][j]) + "\t", end=" ")
            else:
                print(str(board[i][j]))


def place_mines(board, numRowsColumns, numMines):
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


def set_up(board, numRowsColumns, numMines):
    for i in range(numRowsColumns):
        board.append([])
        for j in range(numRowsColumns):
            board[i].append(0)
    board = place_mines(board)
    return board


def test_generation(board, numRowsColumns, numMines):
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
