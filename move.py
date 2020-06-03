import numpy as np
import random


def place(board, player, called):
    placement = list((zip(*np.where(board == called))))
    board[placement[0]] = player
    return board
