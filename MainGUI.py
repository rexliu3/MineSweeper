import pygame
import time
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

def set_up_user_board(emptyBoard, rows, columns):
    for i in range(rows):
        emptyBoard.append([])
        for j in range(columns):
            emptyBoard[i].append(9)
    return emptyBoard

class Grid:
    true_board = []
    true_board = set_up(true_board, rowsNum, columnsNum, minesNum)

    user_board = []
    user_board = set_up_user_board(user_board, rowsNum, columnsNum)

    def __init__(self, rows, columns, width, height):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.model = None
        self.boxes = [[Box(self.user_board[i][j], i, j, width, height) for j in range(columns)] for i in range(rows)]

    def update_model(self):
        self.model = [[self.boxes[i][j].value for j in range(self.columns)] for i in range(self.rows)]

    def select(self, row, column, window):
        pass

    def draw(self, window):
        # Draw Sudoku grid lines
        boxWidth = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(window, mainLinesColor, (0, i * boxWidth), (self.width, i * boxWidth), thick)
            pygame.draw.line(window, mainLinesColor, (i * boxWidth, 0), (i * boxWidth, self.width), thick)
        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.columns):
                self.boxes[i][j].draw(window)

    def click(self, position):
        if position[0] < self.width and position[1] < self.height:
            cubeWidth = self.width / 9
            x = position[0] // cubeWidth
            y = position[1] // cubeWidth
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

    def draw(self, window):
        font = pygame.font.SysFont("times new roman", 40)
        boxWidth = self.width / 9
        x = self.columns * boxWidth
        y = self.rows * boxWidth
        if not (self.value == 9):
            text = font.render(str(self.value), 1, numberColor)
            window.blit(text, (x + (boxWidth / 2 - text.get_width() / 2), y + (boxWidth / 2 - text.get_width() / 2)))

    def set_value(self, value):
        self.value = value


def redraw_window(window, board, time):
    window.fill(backgroundColor)
    # Draw time
    font = pygame.font.SysFont("times new roman", 30)
    text = font.render("Time: " + format_time(time), 1, timeColor)
    window.blit(text, (540 - 170, 560))
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
    width = 540
    height = 540
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("MineSweeper Game")
    board = Grid(rowsNum, columnsNum, width, height)
    key = None
    run = True
    start = time.time()
    while run:
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.solve_board_visual()
                    key = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                clicked = board.click(position)
                if clicked:
                    board.select(clicked[0], clicked[1], window)
                    key = None

        redraw_window(window, board, play_time)
        pygame.display.update()
        board.update_model()

main()
pygame.quit()