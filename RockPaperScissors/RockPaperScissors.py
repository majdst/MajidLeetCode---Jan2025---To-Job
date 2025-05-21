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
    
    #using dictionary instead of conventional method
    
    winnerman = {
        'rock': 'scissor',
        'scissor': 'paper',
        'paper': 'rock'
    }
    
    
    if user == computer:
        print('It is not possible, TIE')
        
    #Important Part of the code:
    
    if winnerman[user] == computer:
        print('User wins')
    else:
        print('Computer wins')
        
    return True
            
    
    
def main():
        
    user = user_choice()
    computer = computer_choice()
        
    game_over = winner(computer, user)

main()