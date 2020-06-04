import all

def main():
    board_player = all.Board().new_board()
    board_computer = all.Board().new_board()
    calling = list(range(1, 26))
    while True:
        called = all.computer_caller(calling)
        all.place(board_player, 0, called)
        all.place(board_computer, 100, called)

        
        if all.check(board_computer) and all.check(board_player):
            return ("It's a tie")
        if all.check(board_computer):
            return ("BINGO!! Computer won")
        if all.check(board_player):
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