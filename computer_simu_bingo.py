import bingo

def main():
    """
    Computer plays with computer
    """
    board_player = bingo.Board().new_board()
    board_computer = bingo.Board().new_board()
    calling = list(range(1, 26))
    while True:
        called = bingo.computer_caller(calling)
        bingo.place(board_player, 0, called)
        bingo.place(board_computer, 100, called)

        
        if bingo.check(board_computer) and bingo.check(board_player):
            return ("It's a tie")
        if bingo.check(board_computer):
            return ("BINGO!! Computer won")
        if bingo.check(board_player):
            return ("BINGO!! Player won")


        
if __name__ == "__main__":
    count_player = 0
    count_computer = 0
    count_tie = 0
    for i in range(100):
        if main() == "BINGO!! Player won":
            count_player += 1
        elif main() == "It's a tie":
            count_tie +=1   
        else:
            count_computer +=1

    print(f"BINGO!! Player won {count_player} times") 
    print(f"BINGO!! Computer won {count_computer} times")  
    print(f"BINGO!! No one won {count_tie} times")       