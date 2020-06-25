# 0-8 Num of Mines
# 9 Unrevealed
# -5 Selected
# -1 Mine

import time

import pygame

from MainGenerator import set_up

pygame.init()
pygame.font.init()

rowsNum = 14
columnsNum = 18
minesNum = 40

# Color Settings
backgroundColor = (255, 255, 255)
selectedBorderColor = (163, 67, 73)
sketchedNumberColor = (224, 202, 203)
numberColor = (179, 120, 123)
mainLinesColor = (213, 166, 169)
timeColor = (179, 120, 123)
wrongCounterColor = (247, 126, 133)


class Grid:
    true_board = []

    def __init__(self, rows, columns, width, height):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.boxes = [[Box(9, i, j, width, height) for j in range(columns)] for i in range(rows)]
        self.model = [[9 for j in range(columns)] for i in range(rows)]
        self.selected = None

    def first_click_generation(self, rows, columns, mines, clickedRow, clickedColumn):
        self.true_board = set_up(self.true_board, rows, columns, mines, clickedRow, clickedColumn)

    def update_model(self):
        self.model = [[self.boxes[i][j].value for j in range(self.columns)] for i in range(self.rows)]

    def reveal(self, rowCoordinate, columnCoordinate, reset_checked=True, oldchecked=[]):
        self.boxes[rowCoordinate][columnCoordinate].set_value(self.true_board[rowCoordinate][columnCoordinate])
        self.update_model()

        if self.boxes[rowCoordinate][columnCoordinate].value != -1:
            if self.boxes[rowCoordinate][columnCoordinate].value == 0:
                board = self.model
                solvedBoard = self.true_board
                rows = len(board)
                columns = len(board[0])
                zeroBoard = []
                # 0 are setup True
                # True means haven't been checked / False means checked

                if reset_checked:
                    zeroBoard = set_up_checked_board(board, zeroBoard)
                else:
                    zeroBoard = oldchecked
                zeroBoard[rowCoordinate][columnCoordinate] = False

                def reveal_surroundings(rowCoordinate, columnCoordinate, zeroBoard):
                    if rowCoordinate != 0 and columnCoordinate != 0 and zeroBoard[rowCoordinate - 1][
                        columnCoordinate - 1]:
                        # if self.boxes[rowCoordinate - 1][columnCoordinate - 1].value == 9:
                        self.reveal(rowCoordinate - 1, columnCoordinate - 1, False, zeroBoard)
                        # self.boxes[rowCoordinate - 1][columnCoordinate - 1].set_value(self.true_board[rowCoordinate - 1][columnCoordinate - 1])

                    if rowCoordinate != 0 and zeroBoard[rowCoordinate - 1][columnCoordinate]:
                        # if self.boxes[rowCoordinate - 1][columnCoordinate].value == 9:
                        self.reveal(rowCoordinate - 1, columnCoordinate, False, zeroBoard)
                        # self.boxes[rowCoordinate - 1][columnCoordinate].set_value(self.true_board[rowCoordinate - 1][columnCoordinate])

                    if rowCoordinate != 0 and columnCoordinate != columns - 1 and zeroBoard[rowCoordinate - 1][
                        columnCoordinate + 1]:
                        # if self.boxes[rowCoordinate - 1][columnCoordinate + 1].value == 9:
                        self.reveal(rowCoordinate - 1, columnCoordinate + 1, False, zeroBoard)
                        # self.boxes[rowCoordinate - 1][columnCoordinate + 1].set_value(self.true_board[rowCoordinate - 1][columnCoordinate + 1])

                    if columnCoordinate != 0 and zeroBoard[rowCoordinate][columnCoordinate - 1]:
                        # if self.boxes[rowCoordinate][columnCoordinate - 1].value == 9:
                        self.reveal(rowCoordinate, columnCoordinate - 1, False, zeroBoard)
                        # self.boxes[rowCoordinate][columnCoordinate - 1].set_value(self.true_board[rowCoordinate][columnCoordinate - 1])

                    if columnCoordinate != columns - 1 and zeroBoard[rowCoordinate][columnCoordinate + 1]:
                        # if self.boxes[rowCoordinate][columnCoordinate + 1].value == 9:
                        self.reveal(rowCoordinate, columnCoordinate + 1, False, zeroBoard)
                        # self.boxes[rowCoordinate][columnCoordinate + 1].set_value(self.true_board[rowCoordinate][columnCoordinate + 1])

                    if rowCoordinate != rows - 1 and columnCoordinate != 0 and zeroBoard[rowCoordinate + 1][
                        columnCoordinate - 1]:
                        # if self.boxes[rowCoordinate + 1][columnCoordinate - 1].value == 9:
                        self.reveal(rowCoordinate + 1, columnCoordinate - 1, False, zeroBoard)
                        # self.boxes[rowCoordinate + 1][columnCoordinate - 1].set_value(self.true_board[rowCoordinate + 1][columnCoordinate - 1])

                    if rowCoordinate != rows - 1 and zeroBoard[rowCoordinate + 1][columnCoordinate]:
                        # if self.boxes[rowCoordinate + 1][columnCoordinate].value == 9:
                        self.reveal(rowCoordinate + 1, columnCoordinate, False, zeroBoard)
                        # self.boxes[rowCoordinate + 1][columnCoordinate].set_value(self.true_board[rowCoordinate + 1][columnCoordinate])

                    if rowCoordinate != rows - 1 and columnCoordinate != columns - 1 and zeroBoard[rowCoordinate + 1][
                        columnCoordinate + 1]:
                        # if self.boxes[rowCoordinate + 1][columnCoordinate + 1].value == 9:
                        self.reveal(rowCoordinate + 1, columnCoordinate + 1, False, zeroBoard)
                        # self.boxes[rowCoordinate + 1][columnCoordinate + 1].set_value(self.true_board[rowCoordinate + 1][columnCoordinate + 1])

                reveal_surroundings(rowCoordinate, columnCoordinate, zeroBoard)
            return True
        else:
            return False

    def select(self, row, column, window):
        # Deselect all cubes
        for i in range(self.rows):
            for j in range(self.columns):
                self.boxes[i][j].selected = False

        self.boxes[row][column].selected = True
        self.selected = (row, column)

    def draw(self, window):
        boxWidth = self.width / columnsNum
        thick = 1

        # Draw Horizontal Lines
        for i in range(self.rows + 1):
            pygame.draw.line(window, mainLinesColor, (0, i * boxWidth), (self.width, i * boxWidth), thick)

        # Draw Vertical Lines
        for i in range(self.columns + 1):
            pygame.draw.line(window, mainLinesColor, (i * boxWidth, 0), (i * boxWidth, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.columns):
                self.boxes[i][j].draw(window)

    def click(self, position):
        if position[0] < self.width and position[1] < self.height:
            boxWidth = self.width / columnsNum
            x = position[0] // boxWidth
            y = position[1] // boxWidth
            return int(y), int(x)
        else:
            return None

    def completed_board(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.boxes[i][j].value == 9:
                    return False
        return True

    def indicate_mine(self, rowCoordinate, columnCoordinate):
        self.boxes[rowCoordinate][columnCoordinate].set_value(-7)

    '''def solve_board_visual(self):
        self.update_model()
        board = self.model

        def reset_checked_board():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0 or board[i][j] == 9 or checking_func(board, i, j) or board[i][j] == -1:
                        checked[i][j] = True
                    else:
                        checked[i][j] = False
            return checked

        def get_first_edge():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != 0 and board[i][j] != 9 and board[i][j] != -1 and not checking_func(board, i, j):
                        return i, j

        def confirm_mine(rowCoordinate, columnCoordinate):
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

        def confirm_safe(rowCoordinate, columnCoordinate):
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

        def next_edge(rowCoordinate, columnCoordinate):
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

        def board_is_solved():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 9:
                        return False
            return True

        def confirmed_mine(rowCoordinate, columnCoordinate):
            # All empty spaces (9) are mines
            rows = len(board)
            columns = len(board[0])
            if rowCoordinate != 0 and columnCoordinate != 0:
                if board[rowCoordinate - 1][columnCoordinate - 1] == 9:
                    self.indicate_mine(rowCoordinate - 1, columnCoordinate - 1)

            if rowCoordinate != 0:
                if board[rowCoordinate - 1][columnCoordinate] == 9:
                    self.indicate_mine(rowCoordinate - 1, columnCoordinate)

            if rowCoordinate != 0 and columnCoordinate != columns - 1:
                if board[rowCoordinate - 1][columnCoordinate + 1] == 9:
                    self.indicate_mine(rowCoordinate - 1, columnCoordinate + 1)

            if columnCoordinate != 0:
                if board[rowCoordinate][columnCoordinate - 1] == 9:
                    self.indicate_mine(rowCoordinate, columnCoordinate - 1)

            if columnCoordinate != columns - 1:
                if board[rowCoordinate][columnCoordinate + 1] == 9:
                    self.indicate_mine(rowCoordinate, columnCoordinate + 1)

            if rowCoordinate != rows - 1 and columnCoordinate != 0:
                if board[rowCoordinate + 1][columnCoordinate - 1] == 9:
                    self.indicate_mine(rowCoordinate + 1, columnCoordinate - 1)

            if rowCoordinate != rows - 1:
                if board[rowCoordinate + 1][columnCoordinate] == 9:
                    self.indicate_mine(rowCoordinate + 1, columnCoordinate)

            if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
                if board[rowCoordinate + 1][columnCoordinate + 1] == 9:
                    self.indicate_mine(rowCoordinate + 1, columnCoordinate + 1)

        def confirmed_safe(rowCoordinate, columnCoordinate):
            # All empty spaces are safe
            rows = len(board)
            columns = len(board[0])
            if rowCoordinate != 0 and columnCoordinate != 0:
                if board[rowCoordinate - 1][columnCoordinate - 1] == 9:
                    self.reveal(rowCoordinate - 1, columnCoordinate - 1)

            if rowCoordinate != 0:
                if board[rowCoordinate - 1][columnCoordinate] == 9:
                    self.reveal(rowCoordinate - 1, columnCoordinate)

            if rowCoordinate != 0 and columnCoordinate != columns - 1:
                if board[rowCoordinate - 1][columnCoordinate + 1] == 9:
                    self.reveal(rowCoordinate - 1, columnCoordinate + 1)

            if columnCoordinate != 0:
                if board[rowCoordinate][columnCoordinate - 1] == 9:
                    self.reveal(rowCoordinate, columnCoordinate - 1)

            if columnCoordinate != columns - 1:
                if board[rowCoordinate][columnCoordinate + 1] == 9:
                    self.reveal(rowCoordinate, columnCoordinate + 1)

            if rowCoordinate != rows - 1 and columnCoordinate != 0:
                if board[rowCoordinate + 1][columnCoordinate - 1] == 9:
                    self.reveal(rowCoordinate + 1, columnCoordinate - 1)

            if rowCoordinate != rows - 1:
                if board[rowCoordinate + 1][columnCoordinate] == 9:
                    self.reveal(rowCoordinate + 1, columnCoordinate)

            if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
                if board[rowCoordinate + 1][columnCoordinate + 1] == 9:
                    self.reveal(rowCoordinate + 1, columnCoordinate)

        def solver_func(rowCoordinate, columnCoordinate):
            if confirm_mine(rowCoordinate, columnCoordinate):
                confirmed_mine(rowCoordinate, columnCoordinate)
                self.update_model()
            if confirm_safe(rowCoordinate, columnCoordinate):
                confirmed_safe(rowCoordinate, columnCoordinate)
                self.update_model()
            checked[rowCoordinate][columnCoordinate] = True

        checked = set_up_checked_board(board, [])
        while not board_is_solved():
            self.update_model()
            row, column = get_first_edge()
            solver_func(row, column)
            while next_edge(row, column):
                self.update_model()
                row, column = next_edge(row, column)
                solver_func(row, column)
            checked = reset_checked_board()'''


class Box:
    def __init__(self, value, rows, columns, width, height):
        self.value = value
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, window):
        font = pygame.font.SysFont("times new roman", 40)
        boxWidth = self.width / columnsNum
        x = self.columns * boxWidth
        y = self.rows * boxWidth
        if not (self.value == 9):
            text = font.render(str(self.value), 1, numberColor)
            window.blit(text, (x + (boxWidth / 2 - text.get_width() / 2), y + (boxWidth / 2 - text.get_width() / 2)))

        if self.selected:
            self.set_background_selected(window)

    def set_value(self, value):
        self.value = value

    def set_background_selected(self, window):
        boxWidth = self.width / columnsNum
        x = self.columns * boxWidth
        y = self.rows * boxWidth

        pygame.draw.line(window, selectedBorderColor, (x, y), (x + boxWidth, y), 2)
        pygame.draw.line(window, selectedBorderColor, (x, y), (x, y + boxWidth), 2)
        pygame.draw.line(window, selectedBorderColor, (x, y + boxWidth), (x + boxWidth, y + boxWidth), 2)
        pygame.draw.line(window, selectedBorderColor, (x + boxWidth, y), (x + boxWidth, y + boxWidth), 2)


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


def set_up_checked_board(board, checked):
    for i in range(len(board)):
        checked.append([])
        for j in range(len(board[0])):
            if board[i][j] == 0 or board[i][j] == 9 or checking_func(board, i, j):
                checked[i].append(True)
            else:
                checked[i].append(False)
    return checked


def redraw_window(window, board, time):
    window.fill(backgroundColor)
    # Draw time
    font = pygame.font.SysFont("times new roman", 30)
    text = font.render("Time: " + format_time(time), 1, timeColor)
    window.blit(text, (board.width - 170, board.height + 15))
    # Draw grid and board
    board.draw(window)


def format_time(seconds):
    second = seconds % 60
    minute = seconds // 60
    hour = minute // 60
    timeFormatted = " " + str(hour) + ":" + str(minute) + ":" + str(second)
    return timeFormatted


def update(inputBoard, window, time):
    inputBoard.update_model()
    redraw_window(window, inputBoard, time)
    pygame.display.update()


def main():
    width = columnsNum * 60
    height = rowsNum * 60
    window = pygame.display.set_mode((width, height + 60))
    pygame.display.set_caption("MineSweeper Game")
    board = Grid(rowsNum, columnsNum, width, height)
    run = True
    key = None
    start = time.time()
    first = True
    while run:
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if first:
                        first = False
                        board.first_click_generation(rowsNum, columnsNum, minesNum, i, j)
                    if not board.reveal(i, j):
                        print("Game over")
                        run = False
                    if board.completed_board():
                        print("You Win")
                        run = False
                if event.key == pygame.K_BACKSPACE:
                    i, j = board.selected
                    board.indicate_mine(i, j)
                if event.key == pygame.K_k:
                    i, j = board.selected
                    if board.boxes[i][j].value == -7:
                        board.boxes[i][j].value = 9
                '''if event.key == pygame.K_SPACE:
                    board.solve_board_visual()
                    run = False'''
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                clicked = board.click(position)
                if clicked:
                    board.select(clicked[0], clicked[1], window)

        redraw_window(window, board, play_time)
        pygame.display.update()
        board.update_model()


main()
pygame.quit()
