def greatest_product(s:str, k:int)->int:

    n = len(s)
    max_prod = 0
    if k< 0 or k > n:
        return 0
    
    prod = 1
    best = 0
    zero_count = 0
    current = 0
    
    #first slide
    first_slide = (s[0:k])
    for i in first_slide:
        if int(i) == 0:
            zero_count +=1
        else:
            prod *= int(i)
    print(f"prod is: {prod}")
    
    best = 0 if zero_count else prod

    #Sliding 
    for j in range(k, n):

        in_d = int(s[j])
        out_d = int(s[j - k])

        #removing right element
        if out_d == 0:
            zero_count -=1
        else:
            prod //= out_d
        #adding left element
        if in_d == 0:
            zero_count += 1
        else:
            prod *= in_d

        current = 0 if zero_count else prod

        print(f'current is {current}')
        if current > best:

            best = current
        
    return best
    


n = greatest_product('23458980812322132130144', 5)
print(n)