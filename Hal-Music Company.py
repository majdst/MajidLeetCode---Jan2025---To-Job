#Make your own music company
def commision_rate():
    sale = float(input('During Last Month, How much did you sell in Total? '))
    
    if sale <= 10000:
        commission = 0.1
    elif 10000 < sale < 15000:
        commission = 0.12
    elif 15000 < sale < 18000:
        commission = 0.14
    elif 18000 < sale < 22000:
        commission = 0.16
    else:
        commission = 0.18
    
    return commission * sale

def main():
    print("Let's See How Much Did You Sell Last Month :)")
    
    in_advance = float(input("How Much Did You Take in Advance Last Month: "))
    
    #checking the validity of in advance
    while in_advance > 2000:
        print('It is not Possible...')
        in_advance = float(input("Please Ask an amount LESS than $2000: "))
    
    commission = commision_rate()
    print(f"The Amount of Commission is {commission}")
    
    pay = commission - in_advance
    
    print(f'The net payment is: {pay:.2f}')

main()