import random

def play():
    user = input("what is your choice? 'r' for Rock, 'p' for Paper, 's' for scissors!! \n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'it\'s a tie'
    
    if is_win(user, computer):
        return 'you won!'
    
    return 'you lost!'
    
    
def is_win(player, opponent):
    #return tru if player wins
    # r > s, s > p, p > r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())