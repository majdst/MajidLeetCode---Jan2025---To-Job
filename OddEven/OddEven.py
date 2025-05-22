import random

def num():
    even = 0
    even_list = []
    odd = 0
    odd_list = []
    number = []
    for i in range(100):
        
        ser = random.randrange(1, 101)
        number.append(ser)
        
        if ser%2 == 0:
            
            even += 1
            even_list.append(ser)
        else:
            odd += 1
            odd_list.append(ser)
            
    print(f'In number list there are {even} even number')
    print(f'In number list there are {odd} odd number')
    
    print(f"Even list: {even_list}")
    print('-------------------------')
    print(f"Odd list: {odd_list}")
    

num()