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

    def add_ship(self, x, y, type = "computer"):
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

def valid_coordinates(x, y, board):
    try:
        x = int(input("Please enter a number: "))
        y = int(input("Please enter a number: "))
        print(f"row = {x} column = {y}")
    except Exception:
        if x > 4 or y >4:
            print("Please enter a number between 0 and 4.")
    except ValueError:
        if float(x) == x or float(y) == y:
            print("Both values have to be integers.")
    else:
        print('Another error has occurred')

def populate_board(board): 
    x = random_point(size)
    y = random_point(size)


def make_guess(board):


def play_game(computer_board, player_board):


def new_game():
    """
    Starts a new game. Sets the board size and numbers of ships, 
    resets the scores and initialises the baords.
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcom to...")
    print(f"Board size is {size}. Number of ships is {num_ships}")
    print("Top left coner is row: 0, col: 0")
    print("-" * 35)
    play_name = input("Please enter your name: \n")
    print("-" * 35)

    computer_board = Board(size, num_ships, "computer", type = "computer")
    player_board = Board(size, num_ships, play_nam, type = "player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)
    





