from final.exception import GameOverException


class Service:
    def __init__(self, repo):
        self.__repo = repo

    def get_board(self):
        return self.__repo.get_board()

    def get_snake(self):
        return self.__repo.get_snake()

    def move(self, dim):
        snake = self.__repo.get_snake()
        board = self.__repo.get_board()
        if self.__repo.direction == "up":
            row = snake[0][0]
            col = snake[0][1]
            while dim > 0:
                apple = 0
                snake.insert(0, [row - 1, col])
                if row == 1:
                    raise GameOverException("you lost")
                if board[row - 1][col].symbol == '+':
                    raise GameOverException("you lost")
                if board[row - 1][col].symbol == '.':
                    apple = 1
                board[row - 1][col].symbol = '*'
                board[row][col].symbol = '+'
                if apple == 0:
                    last_row = snake[-1][0]
                    last_col = snake[-1][1]
                    board[last_row][last_col].symbol = ' '
                    snake.pop()
                if apple == 1:
                    self.__repo.add_new_apple()
                row -= 1
                dim -= 1
        if self.__repo.direction == "right":
            row = snake[0][0]
            col = snake[0][1]
            while dim > 0:
                apple = 0
                snake.insert(0, [row, col + 1])
                if col == self.__repo.dimension - 2:
                    raise GameOverException("you lost")
                if board[row][col + 1].symbol == '+':
                    raise GameOverException("you lost")
                if board[row][col + 1].symbol == '.':
                    apple = 1
                board[row][col + 1].symbol = '*'
                board[row][col].symbol = '+'
                if apple == 0:
                    last_row = snake[-1][0]
                    last_col = snake[-1][1]
                    board[last_row][last_col].symbol = ' '
                    snake.pop()
                if apple == 1:
                    self.__repo.add_new_apple()
                col += 1
                dim -= 1
        if self.__repo.direction == "down":
            row = snake[0][0]
            col = snake[0][1]
            while dim > 0:
                apple = 0
                snake.insert(0, [row + 1, col])
                if row == self.__repo.dimension - 2:
                    raise GameOverException("you lost")
                if board[row + 1][col].symbol == '+':
                    raise GameOverException("you lost")
                if board[row + 1][col].symbol == '.':
                    apple = 1
                board[row + 1][col].symbol = '*'
                board[row][col].symbol = '+'
                if apple == 0:
                    last_row = snake[-1][0]
                    last_col = snake[-1][1]
                    board[last_row][last_col].symbol = ' '
                    snake.pop()
                if apple == 1:
                    self.__repo.add_new_apple()
                row += 1
                dim -= 1
        if self.__repo.direction == "left":
            row = snake[0][0]
            col = snake[0][1]
            while dim > 0:
                apple = 0
                snake.insert(0, [row, col - 1])
                if col == 1:
                    raise GameOverException("you lost")
                if board[row][col - 1].symbol == '+':
                    raise GameOverException("you lost")
                if board[row][col - 1].symbol == '.':
                    apple = 1
                board[row][col - 1].symbol = '*'
                board[row][col].symbol = '+'
                if apple == 0:
                    last_row = snake[-1][0]
                    last_col = snake[-1][1]
                    board[last_row][last_col].symbol = ' '
                    snake.pop()
                if apple == 1:
                    self.__repo.add_new_apple()
                col -= 1
                dim -= 1

    @property
    def board(self):
        return self.__repo