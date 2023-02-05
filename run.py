from random import randint

scores = {"computer": 0, "player": 0}

class Board:
    """
    main board setting of size, player's name, numbers of ships, 
    board type(player's board or computer's). Has methods for 
    adding ships and guesses and print the board
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "x"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, x, type = "computer"):
        if len(self.ship) >= self.num_ships:
            print("Error: you can not add any more ships!")
        else:
            self.ship.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"

def random_point(size):
        """
        return random integer between 0 and size
        """
        return randint(0, size-1)


