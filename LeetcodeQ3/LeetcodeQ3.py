def longchar(s:str)->int:

    n = len(s)
    max_num = 0

    for i in range(n):
        b = set()
        count = 0
        for j in range(i,n):

            if s[j] in b:
                break
            b.add(s[j])
            count += 1

            if count > max_num:
                max_num = count
    return max_num
print(longchar("bb"))