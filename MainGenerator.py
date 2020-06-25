from random import randint


def can_place(row, column, notRow, notColumn, numRows, numColumns):
    # Returns True if can place there
    if row == notRow or column == notColumn:
        return False
    if row != 0 and column != 0 and notRow == row - 1 and notColumn == column - 1:
        return False
    if row != 0 and notRow == row - 1 and notColumn == column:
        return False
    if row != 0 and column != numColumns - 1 and notRow == row - 1 and notColumn == column + 1:
        return False
    if column != 0 and notRow == row and notColumn == column - 1:
        return False
    if column != numColumns - 1 and notRow == row and notColumn == column + 1:
        return False
    if row != numRows - 1 and column != 0 and notRow == row + 1 and notColumn == column - 1:
        return False
    if row != numRows - 1 and notRow == row + 1 and notColumn == column:
        return False
    if row != numRows - 1 and column != numColumns - 1 and notRow == row + 1 and notColumn == column + 1:
        return False

    return True


def place_mines(board, numRows, numColumns, numMines, notRow, notColumn):
    for k in range(numMines):
        rowCoordinate = randint(0, numRows - 1)
        columnCoordinate = randint(0, numColumns - 1)
        while not can_place(rowCoordinate, columnCoordinate, notRow, notColumn, numRows, numColumns):
            rowCoordinate = randint(0, numRows - 1)
            columnCoordinate = randint(0, numColumns - 1)

        while board[rowCoordinate][columnCoordinate] < 0:
            rowCoordinate = randint(0, numRows - 1)
            columnCoordinate = randint(0, numColumns - 1)
        board[rowCoordinate][columnCoordinate] = -1

        if rowCoordinate != 0 and columnCoordinate != 0:
            if board[rowCoordinate - 1][columnCoordinate - 1] >= 0:
                board[rowCoordinate - 1][columnCoordinate - 1] += 1

        if rowCoordinate != 0:
            if board[rowCoordinate - 1][columnCoordinate] >= 0:
                board[rowCoordinate - 1][columnCoordinate] += 1

        if rowCoordinate != 0 and columnCoordinate != numColumns - 1:
            if board[rowCoordinate - 1][columnCoordinate + 1] >= 0:
                board[rowCoordinate - 1][columnCoordinate + 1] += 1

        if columnCoordinate != 0:
            if board[rowCoordinate][columnCoordinate - 1] >= 0:
                board[rowCoordinate][columnCoordinate - 1] += 1

        if columnCoordinate != numColumns - 1:
            if board[rowCoordinate][columnCoordinate + 1] >= 0:
                board[rowCoordinate][columnCoordinate + 1] += 1

        if rowCoordinate != numRows - 1 and columnCoordinate != 0:
            if board[rowCoordinate + 1][columnCoordinate - 1] >= 0:
                board[rowCoordinate + 1][columnCoordinate - 1] += 1

        if rowCoordinate != numRows - 1:
            if board[rowCoordinate + 1][columnCoordinate] >= 0:
                board[rowCoordinate + 1][columnCoordinate] += 1

        if rowCoordinate != numRows - 1 and columnCoordinate != numColumns - 1:
            if board[rowCoordinate + 1][columnCoordinate + 1] >= 0:
                board[rowCoordinate + 1][columnCoordinate + 1] += 1
    return board


def set_up(board, numRows, numColumns, numMines, notRow, notColumn):
    for i in range(numRows):
        board.append([])
        for j in range(numColumns):
            board[i].append(0)
    board = place_mines(board, numRows, numColumns, numMines, notRow, notColumn)
    return board
