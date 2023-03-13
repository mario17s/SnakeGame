import random
import texttable
from domain.entities import Cell


class Board:

    def add_new_apple(self):
        ok_on_board = 0
        while not ok_on_board:
            ap_row = random.randint(0, self.__dimension - 1)
            ap_col = random.randint(0, self.__dimension - 1)
            if ap_row == 0 and ap_col == 0 and self.__board[0][1].symbol != '.' and self.__board[1][0].symbol != '.':
                ok_on_board = 1
                self.__board[ap_row][ap_col].symbol = '.'
                break
            if ap_row == 0 and ap_col == self.__dimension - 1 and self.__board[0][
                self.__dimension - 2].symbol != '.' and self.__board[1][self.__dimension - 1].symbol != '.':
                ok_on_board = 1
                self.__board[ap_row][ap_col].symbol = '.'
                break
            if ap_row == self.__dimension - 1 and ap_col == 0 and self.__board[self.__dimension - 2][0].symbol != '.' and self.__board[self.__dimension - 1][1].symbol != '.':
                ok_on_board = 1
                self.__board[ap_row][ap_col].symbol = '.'
                break
            if ap_row == self.__dimension - 1 and ap_col == self.__dimension - 1 and self.__board[self.__dimension - 1][self.__dimension - 2].symbol != '.' and self.__board[self.__dimension - 2][self.__dimension - 1].symbol != '.':
                ok_on_board = 1
                self.__board[ap_row][ap_col].symbol = '.'
                break
            if ap_row == 0 and self.__board[0][ap_col - 1].symbol != '.' and self.__board[0][ap_col + 1].symbol != '.' and self.__board[1][ap_col].symbol != '.':
                ok_on_board = 1
                self.__board[ap_row][ap_col].symbol = '.'
                break
            if ap_row == self.__dimension - 1 and self.__board[ap_row][ap_col - 1].symbol != '.' and self.__board[ap_row][ap_col + 1].symbol != '.' and self.__board[ap_row - 1][ap_col].symbol != '.':
                ok_on_board = 1
                self.__board[ap_row][ap_col].symbol = '.'
                break
            if ap_col == 0 and self.__board[ap_row - 1][ap_col].symbol != '.' and self.__board[ap_row][ap_col + 1].symbol != '.' and self.__board[ap_row + 1][ap_col].symbol != '.':
                self.__board[ap_row][ap_col].symbol = '.'
                break
            if ap_col == self.__dimension - 1 and self.__board[ap_row - 1][ap_col].symbol != '.' and self.__board[ap_row][ap_col - 1].symbol != '.' and self.__board[ap_row + 1][ap_col].symbol != '.':
                self.__board[ap_row][ap_col].symbol = '.'
                break
            if ap_row != 0 and ap_col != 0 and ap_col != self.__dimension - 1 and ap_row != self.__dimension - 1 and self.__board[ap_row][ap_col].symbol != '*' and self.__board[ap_row][ap_col].symbol != '+' and self.__board[ap_row][ap_col + 1].symbol != '.' and self.__board[ap_row][ap_col - 1].symbol != '.' and self.__board[ap_row + 1][ap_col].symbol != '.' and self.__board[ap_row - 1][ap_col].symbol != '.':
                self.__board[ap_row][ap_col].symbol = '.'
                break


    def __init__(self, file_name = "snake.txt"):
        self.__file_name = file_name
        fin = open(self.__file_name, "rt")
        lines = fin.readlines()
        line1 = lines[0].split("=")
        self.__dimension = int(line1[1].strip())
        line2 = lines[1].split("=")
        self.__apples = int(line2[1].strip())
        self.__board = [[Cell(' ') for i in range (0, self.__dimension)] for j in range(0, self.__dimension)]
        count = 0
        middle = self.__dimension // 2
        self.__board[middle][middle].symbol = '+'
        self.__board[middle - 1][middle].symbol = '*'
        self.__board[middle + 1][middle].symbol = '+'
        self.__snake = []
        self.__snake.append([middle - 1, middle])
        self.__snake.append([middle, middle])
        self.__snake.append([middle + 1, middle])
        self.__direction = "up"
        while count < self.__apples:
            self.add_new_apple()
            count += 1


    @property
    def dimension(self):
        return self.__dimension

    @dimension.setter
    def dimension(self, value):
        self.__dimension = value

    @property
    def apples(self):
        return self.__apples

    @apples.setter
    def apples(self, value):
        self.__apples = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    def get_board(self):
        return self.__board

    def get_snake(self):
        return self.__snake
