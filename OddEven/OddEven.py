import random

#In this version, I am using list comprehension

def oddeven():
    
    numbers = [random.randint(1, 100) for _ in range(100)]
    even_numbers = [n for n in numbers if n%2 ==0]
    odd_numbers = [n for n in numbers if n%2 !=0]
    
    print(f"There are {len(even_numbers)} and the list {even_numbers}")
    print('------------------------------------')
    print(f"There are {len(odd_numbers)} and the list {odd_numbers}")
    
oddeven()
