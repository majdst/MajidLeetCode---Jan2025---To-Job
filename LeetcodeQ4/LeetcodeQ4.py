def median(s:list[int], d:list[int])->float:

    s.extend(d)
    s.sort()
    print(s)
    n = len(s)
    print(n)
    if (n%2) != 0:
        median_index = (n//2)
        #print(s[median_index])
        print(f"the median is {s[median_index]}")
    else:
        median_index = n//2
        print(s[median_index-1])
        print(s[median_index])
        median1 = (s[median_index]+s[median_index-1])
        median2 = median1/2
        print(f"the median is {median2}")

median([1,2,8], [4,5,6])