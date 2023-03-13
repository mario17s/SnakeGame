import texttable

from final.exception import GameOverException


class Game:
    def __init__(self, serv):
        self.__service = serv

    def print_options(self):
        print("move [n]")
        print("up | right | down | left")
        print("exit")

    def display(self):
        t = texttable.Texttable()
        b = self.__service.get_board()
        for i in range(0, self.__service.board.dimension):
            row = []
            for j in range(0, self.__service.board.dimension):
                row.append(b[i][j].symbol)
            t.add_row(row)
        print(t.draw())

    def get_command(self, given_command):
        position = given_command.find(" ")
        if position == -1 and given_command in ["move", "up", "down", "right", "left", "exit"]:
            return given_command, []
        if position != -1:
            command = given_command[:position]
            arguments = given_command[position + 1:]
            arguments = arguments.split(" ")
            if command == "move":
                return command, arguments
        raise ValueError("INVALID COMMAND")

    def move(self, dim = 1):
        try:
            dim = int(dim)
            self.__service.move(dim)
        except ValueError as ve:
            print(ve)

    def up(self):
        if self.__service.board.direction == "down":
            raise ValueError("te dai prea in balene")
        self.__service.board.direction = "up"

    def down(self):
        if self.__service.board.direction == "up":
            raise ValueError("te dai prea in balene")
        self.__service.board.direction = "down"

    def left(self):
        if self.__service.board.direction == "right":
            raise ValueError("te dai prea in balene")
        self.__service.board.direction = "left"

    def right(self):
        if self.__service.board.direction == "left":
            raise ValueError("te dai prea in balene")
        self.__service.board.direction = "right"

    def run_console(self):
        self.display()
        commands={
            "move": self.move,
            "up": self.up,
            "down": self.down,
            "left": self.left,
            "right": self.right
        }
        while True:
            self.print_options()
            given_command = input(">")
            try:
                command, arguments = self.get_command(given_command)
                if command == "exit":
                    break
                print(len(arguments))
                if command == "move" and len(arguments) != 0 and len(arguments) != 1:
                    raise ValueError("too many arguments")

                commands[command](*arguments)
                self.display()
            except ValueError as ve:
                print(ve)
            except GameOverException as goe:
                print(goe)
                break
