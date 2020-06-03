from board import Board
from call import player_caller, computer_caller
from move import place, computer_place
from win_condition import check
import random
import numpy as np


board_player = Board().new_board()
board_computer = Board().new_board()

while True:
    computer_place(board_player, 0)
    if check(board_computer):
        print("Computer won")
        break
    
    computer_place(board_computer, 100)
    if check(board_player):
        print("Player won")
        break


# print(board_computer, "\n", board_player)