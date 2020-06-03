import numpy as np
import random


def place(board, player, position):
    if board[position] == 0:
        print("Already Marked")
        place(board, player, position)
    else:
        board[position] = player
        return board

def computer_place(board, player):
    possibilities = list(zip(*np.where(board != player)))
    if len(possibilities) > 0:
        selection = random.choice(possibilities)
        board[selection] = player
    return board
