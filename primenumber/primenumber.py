import math

def prime(number):
    
    if number <= 1:
        return False
        
    for num in range(2, int(math.sqrt(number)) + 1):
    #
        #print(f'the numbers of : {num}')
        if number % num == 0:
            
            return False
        
    return True

def main():
    
    user_number = int(input('Please Enter a Number: '))
    count = 0
    prime_list = []
    noprime_list = []
    for i in range(2, user_number+1):    
        if prime(i):
            prime_list.append(i)
            count += 1
        else:
            noprime_list.append(i)
    print(f"Number of prime numbers are {count} and list :{prime_list}")


main()