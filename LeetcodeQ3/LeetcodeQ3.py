def longchar(s:str)->int:

    n = len(s)
    max_num = 0
    left = 0
    b = set()
    for right, ch in enumerate(s):
        while ch in b:
            b.remove(s[left])
            print(f'b is: {b}')
            left += 1
        b.add(ch)
        print('*****')
        print(f"b now is: {b}")

    max_num = max(max_num, right - left + 1)

    return max_num

print(longchar("pwwkew"))