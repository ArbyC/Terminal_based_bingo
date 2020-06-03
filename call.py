import random


calling = list(range(1, 26))


def computer_caller(calling):
    if len(calling) != 0:
        random.shuffle(calling)
        return calling.pop()


def player_caller(calling):    
    player_call = input('Enter your call: ')
    if str(player_call) == "Q":
        return "Exit"
    while True:
        try:
            if str(player_call) == "Q":
                return "Exit"
            else:
                while True:
                    if int(player_call) not in calling:
                        print("Already used. Try another number")
                        player_call = input('Enter your call: ')
                        if str(player_call) == "Q":
                            return "Exit"
                    else:
                        return calling.remove(int(player_call))
        except ValueError:
            print("Not a number")
            player_call = input('Enter your call: ')
            if str(player_call) == "Q":
                return "Exit"
        else:
            break