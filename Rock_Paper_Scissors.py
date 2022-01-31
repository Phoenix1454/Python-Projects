import random

def play():
    user = input("Enter Your Choice?, 'p' for Paper, 'r' for Rock, 's' for Scissors!!\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        h = f"It's a Tie, You Chose {user} and Computer also chose {computer} !!"
        return h

    if is_win(user, computer):
        h1 = f"You Won, You Chose {user} and Computer chose {computer} !!"
        return h1

    h2 = f"You Lost, You Chose {user} and Computer chose {computer} !!"
    return h2        

def is_win(user, computer):
    # r > s, s > p, p > r
    # if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
    #     or (user == 'p' and computer == 'r'):
    #     return True
    if(user == 'r' and computer == 's'):
        return True
    elif(user == 's' and computer == 'p'):
        return True
    elif(user == 'p' and computer == 'r'):
        return True
    else:
        return False    

print(play())