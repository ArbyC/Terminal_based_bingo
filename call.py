import random


calling = list(range(1, 26))
def computer_caller(calling):
    if len(calling) != 0:
        random.shuffle(calling)
        return calling.pop()
def user_caller(calling):    
    user_call = input('Enter your call: ')
    if str(user_call) == "Q":
        return "Exit"
    while True:
        try:
            if str(user_call) == "Q":
                return "Exit"
            else:
                while True:
                    if int(user_call) not in calling:
                        print("Already used. Try another number")
                        user_call = input('Enter your call: ')
                        if str(user_call) == "Q":
                            return "Exit"
                    else:
                        return calling.remove(int(user_call))
        except ValueError:
            print("Not a number")
            user_call = input('Enter your call: ')
            if str(user_call) == "Q":
                return "Exit"
        else:
            break