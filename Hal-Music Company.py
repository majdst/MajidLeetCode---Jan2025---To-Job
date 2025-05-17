#Make your own music company
def commision_rate():
    sale = float(input('During Last Month, How much did you sell in Total? '))
    
    sale_dic = {
        10000 : 0.1,
        15000 : 0.12,
        18000 : 0.14,
        22000 : 0.16
        
    }
    
    for i in sorted(sale_dic):
        
        if sale <= i:
            return sale_dic[i]
    return 0.18
        

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