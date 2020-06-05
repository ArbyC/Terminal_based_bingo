from board import Board
from call import player_caller, computer_caller
from move import place
from win_condition import check
import random
import numpy as np


def main(board_type):
    

    if board_type.lower() == "y":
        board_player = Board().write_board()
    elif board_type.lower() == "n":
        board_player = Board().new_board()
    else:
        print("I didn't understand. Restart.")
        exit()
    print("\n WELCOME TO BINGO")
    print("\n    NEW GAME \n Enter Q to quit\n")
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