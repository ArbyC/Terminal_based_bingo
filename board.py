import random
import numpy as np

class Board():
    def __init__(self, board=None):
        self.board = np.zeros((5,5), dtype=int)

    def write_board(self):
        entry = input("Make your board row wise: ").split(",")[0:25]
        try:
            user_numbers = [int(i) for i in entry if int(i) < 26]
        except ValueError:
            return "Enter numbers only"
        if list(set(user_numbers)) == user_numbers:
            try:
                user_numbers = np.array(user_numbers).reshape(5,5)
            except ValueError:
                return "Not a valid input. Check if you have non repeated 25 numbers spearated by commas upto 25."
            return user_numbers
        else:
            return "Numbers are repeated"

    def new_board(self):
        self.board = np.arange(1,26)
        random.shuffle(self.board)
        return (self.board).reshape(5,5)

