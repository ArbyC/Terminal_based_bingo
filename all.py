import numpy as np
import sys 
import random


class Board():
    def __init__(self, board=None):
        self.board = np.zeros((5,5), dtype=int)

    def write_board(self):
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
                    entry = input("Row spearated by comma: ").split(",")
                    if "Q" in entry: exit()
                else:
                    break
            written_board = written_board + user_numbers
            print(written_board)
        written_board = np.array(written_board).reshape(5,5)
        return written_board

    def new_board(self):
        self.board = np.arange(1,26)
        random.shuffle(self.board)
        return (self.board).reshape(5,5)


def place(board, player, called):
    placement = list((zip(*np.where(board == called))))
    board[placement[0]] = player
    return board

def computer_caller(calling):
    if len(calling) != 0:
        random.shuffle(calling)
        return calling.pop()


def player_caller(calling):    
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

def row_win(x):
    if np.all(x==0) or np.all(x==100):
        return 1
    else:
        return 0

def col_win(x):
    if np.all(x==0) or np.all(x==100):
        return True
    else:
        return False

def diag_win(board):
    if np.all(np.diag(board)==0) or np.all(np.diag(board)==100):
        a = 1
    else:
        a = 0

    if np.all(np.diag(np.fliplr(board))==0) or np.all(np.diag(np.fliplr(board))==100):
        a +=1
    else:
        a +=0
    return a

def check(board):
    row_check = np.apply_along_axis(row_win, axis=1, arr=board)
    col_check = np.apply_along_axis(col_win, axis=1, arr=board)
    diag_check = diag_win(board)
    chk = sum(row_check) + sum(col_check) + diag_check
    if chk >= 5:
        return True
    else:
        return False

def main():
    board_player = Board().new_board()
    board_computer = Board().new_board()
    calling = list(range(1, 26))
    i = 2


    while True:
        if i % 2 == 0:
            print(board_player)
            called = player_caller(calling)
            i +=1
        else:
            called = computer_caller(calling)
            i += 1
        place(board_player, 0, called)
        if check(board_player):
            print("BINGO!! Player won")
            break
        place(board_computer, 100, called)
        if check(board_computer):
            print("BINGO!! Computer won")
            break
        
    


if __name__ == "__main__":
    main()