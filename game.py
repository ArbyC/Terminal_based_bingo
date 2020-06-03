from board import Board
from call import player_caller, computer_caller
from move import place, computer_place
from win_condition import row_win, col_win, diag_win
import random
import numpy as np


board_player = Board().new_board()
board_computer = Board().new_board()

for i in range(15):
    computer_place(board_player, 0)
    check_player = [row_win(board_player, 0), col_win(board_player, 0), diag_win(board_player, 0)]
    computer_place(board_computer, 100)
    check_computer = [row_win(board_computer, 100), col_win(board_computer, 100), diag_win(board_computer, 100)]


print(board_computer, "\n", board_player)
print(check_player, '\n', check_computer)