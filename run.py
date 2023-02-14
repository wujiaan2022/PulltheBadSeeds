from random import randint

scores = {"neighbor": 0, "player": 0}


class Board:
    """
    main board setting of size, player's name, numbers of bad seeds,
    board type(player's board or neighbor's). Has methods for
    adding bad seeds and guesses and print the board
    """
    def __init__(self, size, num_bad_seeds, name, type):
        self.size = size
        self.board = [[". " for x in range(size)] for y in range(size)]
        self.num_bad_seeds = num_bad_seeds
        self.name = name
        self.type = type
        self.guess_place = []
        self.add_place = []
        self.rand_place = []

    def print(self):
        """
        print the board
        """
        for row in self.board:
            print(" ".join(row))

    def add_seeds(self):
        """
        Use while loop to add random and non-repeating coordinate (bad seeds)
        in both garden. Print a symbol ! on player side while computer side is
        hidden. Note: in test version, both side are shown. After tested, will
        add "if self.type == "player":"in front of the last line
        (last line indent).
        """
        while len(self.add_place) < self.num_bad_seeds:
            add_row = randint(0, self.size-1)
            add_col = randint(0, self.size-1)
            add_coord = [add_row, add_col]
            if add_coord not in self.add_place:
                self.add_place.append([add_row, add_col])
                if self.type == "player":
                    self.board[add_row][add_col] = "# "

    def my_guess(self):
        """
        The outer while loop includes two sub while loop which promp player
        to make a guess row and col, and validate the both.
        Then in outer loop, outside the subloops to validate the guess
        coordinat, if it's not already guessed, then move on to hit or miss
        part which is outside the outer loop. if hit, shown as $ and increment
        the score. If miss shown as x.
        """
        num = self.size-1

        while True:
            str1 = "Guess a number between 0 and"
            str2 = "Hei, you are in my garage!"
            str3 = "come back to my garden."
            str4 = "Your number must be between 0 and"
            str5 = "You dig that place already neighbor,"
            while True:
                print("\nPlease guess a row number:")
                try:
                    guess_row = int(input(f"{str1} {num}\n"))
                    if guess_row <= num:
                        break
                    elif guess_row > num:
                        print(f"\n{str2} \n{str3}\n{str4} {num}.")
                except ValueError:
                    print("\nYou can only enter a interger number!")

            while True:
                print("\nPlease guess a column number:")
                try:
                    guess_col = int(input(f"{str1} {num}\n"))
                    if guess_col <= num:
                        break
                    elif guess_col > num:
                        print(f"\n{str2} \n{str3}\n{str4} {num}.")
                except ValueError:
                    print("\nYou can only enter a interger number!")

            guess_coord = [guess_row, guess_col]
            if guess_coord in self.guess_place:
                print(f"{str5} \nplease choose a different spot.")
            else:
                break

        guess_coord = [guess_row, guess_col]
        self.guess_place.append(guess_coord)
        if guess_coord in self.add_place:
            self.board[guess_row][guess_col] = "$ "
            print("\nYou got it! Now your neighbor can plant flowers.")
            scores["player"] += 1
        else:
            self.board[guess_row][guess_col] = "X "
            print("\nYou missed, don't give up, keep going!")

    def neighbor_rand_guess(self):
        """
        Through a while loop, computer makes random non-repeating coordinate.
        Outside the loop, if the coordinate hit, print $ and increment score.
        Otherwise print X
        """
        while True:
            rand_row = randint(0, self.size-1)
            rand_col = randint(0, self.size-1)
            rand_coord = [rand_row, rand_col]
            if rand_coord not in self.rand_place:
                self.rand_place.append([rand_row, rand_col])
                break
        if rand_coord in self.add_place:
            self.board[rand_row][rand_col] = "$ "
            print("\nYour neighbor got it! Now you can plant flowers.")
            scores["neighbor"] += 1
        else:
            self.board[rand_row][rand_col] = "X "
            print("\nYour neighbor missed, but she/he will keep going!")


def new_game():
    """
    Starts a new game. Sets the board size and numbers of bad seeds,
    resets the scores and print the baords and random bad seeds.
    Use while loop to start the game, player guesses and computer
    make random coord.Game will automatic stop when one side's score
    reach the number of bad seeds. Then winner will be announced and
    this round game over.
    """
    size = 4
    num_bad_seeds = 3
    scores["neighbor"] = 0
    scores["player"] = 0
    print("-" * 20)
    str6 = "Welcom! You and your neighbor will help each other"
    str7 = "to dig out bad seeds from your garden!"
    str8 = "Your garden size is"
    print(f"\n{str6} \n{str7} \nIsn't that exciting!")
    print(f"{str8} {size}. \nNumber of bad seeds is {num_bad_seeds}")
    print("Top left coner is row: 0, col: 0")
    print("-" * 20)
    play_name = input("Please enter your name:\n")
    print("-" * 20)

    neighbor_board = Board(size, num_bad_seeds, "neighbor", type="neighbor")
    player_board = Board(size, num_bad_seeds, play_name, type="player")

    print("\nneighbor's garden")
    print()
    neighbor_board.add_seeds()
    neighbor_board.print()
    print(f"\n{play_name}'s garden")
    print()
    player_board.add_seeds()
    player_board.print()

    while True:

        neighbor_board.my_guess()
        my_score = scores["player"]
        print(f"Your current score is: {my_score}")
        print("\nYour neighbor's garden")
        neighbor_board.print()

        player_board.neighbor_rand_guess()
        neighbor_score = scores["neighbor"]
        print(f"Her/his current score is: {neighbor_score}")
        print(f"\n{play_name}'s garden")
        player_board.print()

        if scores["player"] == num_bad_seeds or scores["neighbor"] == num_bad_seeds:
            break

    str9 = "In this round you win! But he/she is not sad at all."
    str10 = "In fact, he/she will bring you a big bucket of icecream!"
    str11 = "But your garden will be prettier, so it's win_win!"
    print("\nGame Over!")
    if my_score > neighbor_score:
        print(f"{str9} \n{str10}")
    elif my_score == neighbor_score:
        print("In this round you are even!")
    elif my_score < neighbor_score:
        print(f"In this round your neighber win! \n{str11}")


def game_round():
    """
    Player will be asked for another round. when yes start a new game.
    when no exit the game.
    """
    while True:
        new_game()
        a = input("\nWould you like another round? any key or n\n")
        a = a.lower()
        if a != "n":
            continue
        elif a == "n":
            break


game_round()
