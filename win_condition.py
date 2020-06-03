import numpy as np


def row_win(board, player):
    if np.any(np.all(board==player, axis=1)):
        return True
    else:
        return False

def col_win(board, player):
    if np.any(np.all(board==player, axis=0)):
        return True
    else:
        return False

def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        return True
    else:
        return False