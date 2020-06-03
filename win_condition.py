import numpy as np


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