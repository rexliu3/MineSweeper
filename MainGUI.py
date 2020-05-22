import pygame

pygame.init()
pygame.font.init()

# 24 - 99 / 18 - 40 / 10 - 10
numRowsColumns = 10
numMines = 10

'''class Grid:
    # 0-8 = num
    # -1 = bombs
    # 9 = unrevealed
    board = [
        [0, 0, 1, 9, 9, 9, 9, 9, 9, 9], 
        [0, 0, 1, 9, 9, 9, 9, 9, 9, 9], 
        [2, 2, 1, 9, 9, 9, 9, 9, 9, 9], 
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
    ]
    
    #board = set_up(board, numRowsColumns, numMines)
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.boxes = [[Box(self.board[i][j], i, j, width, height, True if ) for j in range(numRowsColumns)] for i in range(numRowsColumns)]
        


class Box:
    def __init__(self, row, column, width, height):
        self.isBomb = False
        self.revealed = False

def main():
    pass

main()'''
