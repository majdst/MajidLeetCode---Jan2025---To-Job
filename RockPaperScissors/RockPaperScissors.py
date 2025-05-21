import random

def computer_choice():
    
    num = random.randrange(1,4)
    
    if num == 1:
        return 'rock'
    
    if num == 2:
        return 'paper'
    
    if num == 3:
        return 'scissor'
    
def user_choice():
    
    return input('Please Enter User choice: ').strip().lower()

def winner(computer, user):
    
    print(f'\n computer choice is: {computer}')
    print(f'User choice is: {user}')
    
    if user == computer:
        print('It is not possible')
        return False
    #Important Part of the code:
    
    if (user == 'Rock' and computer == 'scissors') or \
        (user == 'scissors' and computer == 'player') or \
            (user == 'paper' and computer == 'rock'):
                print('User wins')
    else:
        print('Computer wins')
        
    return True
            
    
    
def main():
    
    game_over = False
    
    while not game_over:
        
        user = user_choice()
        computer = computer_choice()
        
        game_over = winner(computer, user)

main()