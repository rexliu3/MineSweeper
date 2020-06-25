# 0-8 Num of Mines
# 9 Unrevealed
# -5 Selected
# -1 Mine

import pygame
import time
from MainGenerator import set_up
from MainSolver import set_up_checked_board
from MainSolver import checking_func as is_edge

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
    true_board = set_up(true_board, rowsNum, columnsNum, minesNum)

    def __init__(self, rows, columns, width, height):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.boxes = [[Box(9, i, j, width, height) for j in range(columns)] for i in range(rows)]
        self.model = [[9 for j in range(columns)] for i in range(rows)]
        self.selected = None

    def update_model(self):
        self.model = [[self.boxes[i][j].value for j in range(self.columns)] for i in range(self.rows)]

    def reveal(self):
        rowCoordinate, columnCoordinate = self.selected
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

                zeroBoard = set_up_checked_board(board, zeroBoard)
                zeroBoard[rowCoordinate][columnCoordinate] = False
                if True:
                    def check_right(board, rowCoordinate, columnCoordinate):
                        if columnCoordinate != columns - 1 and solvedBoard[rowCoordinate][
                            columnCoordinate + 1] == 0 and zeroBoard[rowCoordinate][columnCoordinate + 1]:
                            self.boxes[rowCoordinate][columnCoordinate + 1].set_value(0)
                            zeroBoard[rowCoordinate][columnCoordinate + 1] = False
                            check_right(board, rowCoordinate, columnCoordinate + 1)
                            check_up(board, rowCoordinate, columnCoordinate + 1)
                            check_down(board, rowCoordinate, columnCoordinate + 1)
                            '''elif columnCoordinate != columns - 1:
                            self.boxes[rowCoordinate][columnCoordinate + 1].set_value(
                                self.true_board[rowCoordinate][columnCoordinate + 1])'''

                    def check_left(board, rowCoordinate, columnCoordinate):
                        if columnCoordinate != 0 and solvedBoard[rowCoordinate][columnCoordinate - 1] == 0 and \
                                zeroBoard[rowCoordinate][
                                    columnCoordinate - 1]:
                            self.boxes[rowCoordinate][columnCoordinate - 1].set_value(0)
                            zeroBoard[rowCoordinate][columnCoordinate - 1] = False
                            check_left(board, rowCoordinate, columnCoordinate - 1)
                            check_up(board, rowCoordinate, columnCoordinate - 1)
                            check_down(board, rowCoordinate, columnCoordinate - 1)
                            '''elif columnCoordinate != 0:
                            self.boxes[rowCoordinate][columnCoordinate - 1].set_value(
                                self.true_board[rowCoordinate][columnCoordinate - 1])'''

                    def check_up(board, rowCoordinate, columnCoordinate):
                        if rowCoordinate != 0 and solvedBoard[rowCoordinate - 1][columnCoordinate] == 0 and \
                                zeroBoard[rowCoordinate - 1][columnCoordinate]:
                            self.boxes[rowCoordinate - 1][columnCoordinate].set_value(0)
                            zeroBoard[rowCoordinate - 1][columnCoordinate] = False
                            check_right(board, rowCoordinate - 1, columnCoordinate)
                            check_left(board, rowCoordinate - 1, columnCoordinate)
                            check_up(board, rowCoordinate + 1, columnCoordinate)
                            '''elif rowCoordinate != 0:
                            self.boxes[rowCoordinate - 1][columnCoordinate].set_value(
                                self.true_board[rowCoordinate - 1][columnCoordinate])'''

                    def check_down(board, rowCoordinate, columnCoordinate):
                        if rowCoordinate != rows - 1 and solvedBoard[rowCoordinate + 1][columnCoordinate] == 0 and \
                                zeroBoard[rowCoordinate + 1][columnCoordinate]:
                            self.boxes[rowCoordinate + 1][columnCoordinate].set_value(0)
                            zeroBoard[rowCoordinate + 1][columnCoordinate] = False
                            check_right(board, rowCoordinate + 1, columnCoordinate)
                            check_left(board, rowCoordinate + 1, columnCoordinate)
                            check_down(board, rowCoordinate - 1, columnCoordinate)
                            '''elif rowCoordinate != rows - 1:
                            self.boxes[rowCoordinate + 1][columnCoordinate].set_value(
                                self.true_board[rowCoordinate + 1][columnCoordinate])'''

                    check_right(board, rowCoordinate, columnCoordinate)
                    check_left(board, rowCoordinate, columnCoordinate)
                    check_down(board, rowCoordinate, columnCoordinate)
                    check_up(board, rowCoordinate, columnCoordinate)
                if True:
                    def first_edge_zero():
                        self.update_model()
                        for i in range(rowsNum):
                            for j in range(columnsNum):
                                if self.boxes[i][j].value == 0 and not is_edge(board, i, j) and has_zero_edge():
                                    return i, j

                    def move_edge_zero(rowCoordinate, columnCoordinate):
                        reveal_surroundings(rowCoordinate, columnCoordinate)
                        zeroBoard[rowCoordinate][columnCoordinate] = False
                        if rowCoordinate != 0:
                            if self.boxes[rowCoordinate - 1][
                                columnCoordinate].value == 0:  # and not is_edge(board, rowCoordinate - 1, columnCoordinate):
                                if zeroBoard[rowCoordinate - 1][columnCoordinate]:
                                    reveal_surroundings(rowCoordinate - 1, columnCoordinate)
                                    zeroBoard[rowCoordinate - 1][columnCoordinate] = False
                                    move_edge_zero(rowCoordinate - 1, columnCoordinate)

                        if columnCoordinate != columns - 1:
                            if self.boxes[rowCoordinate][columnCoordinate + 1].value == 0:
                                if zeroBoard[rowCoordinate][
                                    columnCoordinate + 1]:  # and not is_edge(board, rowCoordinate, columnCoordinate + 1):
                                    reveal_surroundings(rowCoordinate, columnCoordinate + 1)
                                    zeroBoard[rowCoordinate][columnCoordinate + 1] = False
                                    move_edge_zero(rowCoordinate, columnCoordinate + 1)

                        if rowCoordinate != rows - 1:
                            if self.boxes[rowCoordinate + 1][
                                columnCoordinate].value == 0:  # and not is_edge(board, rowCoordinate + 1, columnCoordinate):
                                if zeroBoard[rowCoordinate + 1][columnCoordinate]:
                                    reveal_surroundings(rowCoordinate + 1, columnCoordinate)
                                    zeroBoard[rowCoordinate + 1][columnCoordinate] = False
                                    move_edge_zero(rowCoordinate + 1, columnCoordinate)

                        if columnCoordinate != 0:
                            if self.boxes[rowCoordinate][
                                columnCoordinate - 1].value == 0:  # and not is_edge(board, rowCoordinate, columnCoordinate - 1):
                                if zeroBoard[rowCoordinate][columnCoordinate - 1]:
                                    reveal_surroundings(rowCoordinate, columnCoordinate - 1)
                                    zeroBoard[rowCoordinate][columnCoordinate - 1] = False
                                    move_edge_zero(rowCoordinate, columnCoordinate - 1)

                    def reveal_surroundings(rowCoordinate, columnCoordinate):
                        if rowCoordinate != 0 and columnCoordinate != 0:
                            # if self.boxes[rowCoordinate - 1][columnCoordinate - 1].value == 9:
                            self.boxes[rowCoordinate - 1][columnCoordinate - 1].set_value(
                                self.true_board[rowCoordinate - 1][columnCoordinate - 1])

                        if rowCoordinate != 0:
                            # if self.boxes[rowCoordinate - 1][columnCoordinate].value == 9:
                            self.boxes[rowCoordinate - 1][columnCoordinate].set_value(
                                self.true_board[rowCoordinate - 1][columnCoordinate])

                        if rowCoordinate != 0 and columnCoordinate != columns - 1:
                            # if self.boxes[rowCoordinate - 1][columnCoordinate + 1].value == 9:
                            self.boxes[rowCoordinate - 1][columnCoordinate + 1].set_value(
                                self.true_board[rowCoordinate - 1][columnCoordinate + 1])

                        if columnCoordinate != 0:
                            # if self.boxes[rowCoordinate][columnCoordinate - 1].value == 9:
                            self.boxes[rowCoordinate][columnCoordinate - 1].set_value(
                                self.true_board[rowCoordinate][columnCoordinate - 1])

                        if columnCoordinate != columns - 1:
                            # if self.boxes[rowCoordinate][columnCoordinate + 1].value == 9:
                            self.boxes[rowCoordinate][columnCoordinate + 1].set_value(
                                self.true_board[rowCoordinate][columnCoordinate + 1])

                        if rowCoordinate != rows - 1 and columnCoordinate != 0:
                            # if self.boxes[rowCoordinate + 1][columnCoordinate - 1].value == 9:
                            self.boxes[rowCoordinate + 1][columnCoordinate - 1].set_value(
                                self.true_board[rowCoordinate + 1][columnCoordinate - 1])

                        if rowCoordinate != rows - 1:
                            # if self.boxes[rowCoordinate + 1][columnCoordinate].value == 9:
                            self.boxes[rowCoordinate + 1][columnCoordinate].set_value(
                                self.true_board[rowCoordinate + 1][columnCoordinate])

                        if rowCoordinate != rows - 1 and columnCoordinate != columns - 1:
                            # if self.boxes[rowCoordinate + 1][columnCoordinate + 1].value == 9:
                            self.boxes[rowCoordinate + 1][columnCoordinate + 1].set_value(
                                self.true_board[rowCoordinate + 1][columnCoordinate + 1])

                    def reset_checked_board():
                        self.update_model()
                        for i in range(len(board)):
                            for j in range(len(board[0])):
                                if self.boxes[i][j].value == 0 and not is_edge(board, i, j):
                                    zeroBoard[i][j] = True
                                else:
                                    zeroBoard[i][j] = False
                        return zeroBoard

                    self.update_model()
                    zeroBoard = reset_checked_board()
                    row, column = first_edge_zero()
                    reveal_surroundings(row, column)
                    zeroBoard[row][column] = False
                    self.update_model()
                    move_edge_zero(row, column)
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

    def solve_board_visual(self):
        pass


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
    while run:
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.solve_board_visual()
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if not board.reveal():
                        print("Game over")
                        # run = False
                    if board.completed_board():
                        print("You Win")
                        run = False
                if event.key == pygame.K_BACKSPACE:
                    i, j = board.selected
                    board.boxes[i][j].value = -5
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
