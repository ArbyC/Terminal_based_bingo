from board import Board
from call import player_caller, computer_caller
from move import place
from win_condition import check
import random
import numpy as np


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