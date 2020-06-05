import numpy as np
import sys 
import random


# Board Class #
class Board():
    """
    Bingo board class with manual and random board method
    """
    def __init__(self, board=None):
        """
        Constructor for board
        """ 
        self.board = np.zeros((5,5), dtype=int)

    def write_board(self):
        """
        Writes user defined board taking 1 row input at a time
        Enter Q to exit game
        """
        availiable = set(range(1,26))
        print(f"Numbers avaliable to write are {availiable}")
        written_board = []
        for i in range(5):
            while True:
                try:
                    user_numbers = []
                    count = 0
                    while len(user_numbers) !=5:
                        if count != 0:
                            print("Your input was repeated or invalid")    
                        entry = input("Row spearated by comma: ").split(",")
                        if "Q" in entry: exit()
                        user_numbers = [int(i) for i in entry if (int(i) < 26 and int(i) not in written_board)]
                        count += 1

                except ValueError:
                    print("Enter numbers only")
                    if "Q" in entry: exit()
                else:
                    break
            written_board = written_board + user_numbers
            print(f"Numbers you already wrote are {set(written_board)}")
            availiable = availiable - set(written_board)
            print(f"Numbers remaining are {availiable}")
        written_board = np.array(written_board).reshape(5,5)
        return written_board

    def new_board(self):
        """
        Randomly generates a board with numbers in range 1-26
        """
        self.board = np.arange(1,26)
        random.shuffle(self.board)
        return (self.board).reshape(5,5)


# Placing in board #
def place(board, player, called):
    """
    Places the called number if not already place else raises IndexError and calls again"
    """
    placement = list((zip(*np.where(board == called))))
    try:
        board[placement[0]] = player
    except IndexError:
        print(f"The called value is {called}, the board is like this {board}, the player is {player}")
    return board


# Calling a value to be placed in board #
def computer_caller(calling):
    """
    Randomly calls a number from the list of number
    """
    if len(calling) != 0:
        random.shuffle(calling)
        return calling.pop()


def player_caller(calling):    
    """
    Calls the number player inputs
    """
    player_call = input('Enter your call: ')
    if str(player_call) == "Q": return exit() 
    while True:
        try:
            if str(player_call) == "Q": return exit() 
            else:
                while True:
                    if int(player_call) not in calling:
                        print("Already used. Try another number")
                        player_call = input('Enter your call: ')
                        if str(player_call) == "Q": return exit() 
                    else:
                        calling.remove(int(player_call))
                        return int(player_call)
        except ValueError:
            print("Not a number")
            player_call = input('Enter your call: ')
            if str(player_call) == "Q": return exit() 
        else:
            break


# Win conditions #
def row_win(x):
    """
    Row win conditon for computer and player
    """
    if np.all(x==0) or np.all(x==100):
        return 1
    else:
        return 0

def col_win(x):
    """
    column win conditon for computer and player
    """
    if np.all(x==0) or np.all(x==100):
        return True
    else:
        return False

def diag_win(board):
    """
    Diagonal win conditon for computer and player
    """
    if np.all(np.diag(board)==0) or np.all(np.diag(board)==100):
        a = 1
    else:
        a = 0

    if np.all(np.diag(np.fliplr(board))==0) or np.all(np.diag(np.fliplr(board))==100):
        a +=1
    else:
        a +=0
    return a


# Win check #
def check(board):
    """
    Check if someone has won
    """
    row_check = np.apply_along_axis(row_win, axis=1, arr=board)
    col_check = np.apply_along_axis(col_win, axis=1, arr=board)
    diag_check = diag_win(board)
    chk = sum(row_check) + sum(col_check) + diag_check
    if chk >= 5:
        return True
    else:
        return False


def main(board_type):
    """
    Main game starts here
    """
    print("\n WELCOME TO BINGO")
    print("\n    NEW GAME \n Enter Q to quit\n")

    if board_type.lower() == "y":
        board_player = Board().write_board()
    elif board_type.lower() == "n":
        board_player = Board().new_board()
    else:
        print("I didn't understand. Restart.")
        exit()
    board_computer = Board().new_board()
    calling = list(range(1, 26))
    i = 2

    while True:
        if i % 2 == 0:
            print(board_player,"\n")
            called = player_caller(calling)
            i +=1
        else:
            called = computer_caller(calling)
            i += 1
        place(board_player, 0, called)

        if check(board_computer) and check(board_player):
            return ("It's a tie")

        if check(board_player):
            print("BINGO!! Player won")
            break
        place(board_computer, 100, called)
        if check(board_computer):
            print("BINGO!! Computer won")
            break
        
    
if __name__ == "__main__":
    board_type = input("Wanna create your own board(Y/N)?: ")
    while True:
        main(board_type)
