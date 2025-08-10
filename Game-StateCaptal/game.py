import random

def main():

    usa_state = {'Alabama': 'Montgomery', 'Alaska': 'Jeneau',
                 'Arizona': 'Phoenix', 'Arkansas': 'LittleRock',
                 'California':'Sacramento', 'Colorado':'Denver',
                 'Connecticut':'Hartford', 'Delaware':'Dover',
                 'Florida': 'Tallahassee', 'Georgia':'Atlanta',
                 'Hawaii':'Honolulu', 'Idaho':'Boise',
                 'Illinois':'Springfield', 'Indiana':'Indianapolis',
                 'Iowa':'Des Moines', 'Kansas':'Topeka',
                 'Kentucky': 'Frankfort', 'Louisiana':'Baton Rouge',
                 'Maine':'Augusta', 'Maryland':'annapolis',
                 'Massachusetts':'Boston', 'Michigan':'Lansing',
                 'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                 'Missouri':'Jefferson City', 'Montana':'Helena',
                 'Nebraska':'Lincoln', 'Nevada':'Carson City',
                 'New Hampshire':'Concord', 'New Jersey':'Trenton',
                 'New Mexico': 'SantaFe', 'Newyork':'Albany',
                 'NorthCarolina':'Raleigh', 'North Dakota':'Bismark',
                 'Ohio': 'Columbus', 'Oklahoma':'Oklahoma City',
                 'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                 'Rhode Island':'Providence', 'South Carolina':'Columbia',
                 'South Dakota':'Pierre', 'Tennessee':'Nashville',
                 'Texas':'Austin', 'Utah':'Salt Lake City',
                 'Vermont':'Montpelier', 'Virginia':'Richmond',
                 'Washington':'Olympia', 'West Virginia':'Charleston',
                 'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    
    correct, wrong = state_captal(usa_state)

    print(f'Correct answ is {correct}, wrong answ is {wrong}')
def state_captal(dct_in):

    corr_ans = 0
    wrng_ans = 0
    num_question = int(input('How many questions do you want to be asked? '))

    for i in range(num_question):
        # randomly choose the state
        state_name = random.choice(list(dct_in.keys()))

        print(f'Q{i}: Captal of {state_name} is: ')
        user_captal = input('Please write your answer: ').lower()

        if user_captal == dct_in[state_name].strip().lower():

            print('Correct!')
            corr_ans += 1
        else:
            print('Incorrect!')
            wrng_ans += 1
    return corr_ans, wrng_ans

main()