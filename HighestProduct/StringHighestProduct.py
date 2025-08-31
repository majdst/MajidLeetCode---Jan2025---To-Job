def max_product(s:str, k:int)-> int:

    #length s
    n = len(s)

    product = 1
    zero_comb = 0

    #sanity check
    if k<0 or k>n:
        return 0
    
    #First slide
    for i in range(k):
        first_slide = int(s[i])

        #check if there is zero or not
        if first_slide == 0:

            zero_comb += 1
        else:
            product *= first_slide
    
    best_product = product

    #Sliding one to right
    for j in range(k, n):

        d_in = int(s[j])
        d_out = int(s[j-k])

        # removing first element
        if d_out == 0:

            zero_comb -=1
        else:
            product //= d_out
        #Adding new element
        if d_in == 0:
            zero_comb += 1
        else:
            product *= d_in

        
        if product > best_product:

            best_product = product

    return best_product

print(max_product('123834539327238239583', 5))