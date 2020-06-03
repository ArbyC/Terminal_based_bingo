import random
import numpy as np

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

    

