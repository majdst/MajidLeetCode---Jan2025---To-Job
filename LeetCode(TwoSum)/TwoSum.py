#testGiven an array of integers nums and
# an integer target, return indices of the
#  two numbers such that they add up to target.

list_desig = []
def gather_user():

    how_many = int(input('How many numbers do you wanna add: '))
    while len(list_desig) < how_many:

        user_numb = int(input('Please add number: '))
        list_desig.append(user_numb)
    return list_desig

def main():
    # list1 = gather_user()
    # print('What will be the target? ')
    # target = int(input('Target: '))
    # #BrutForce 
    # for i in range(len(list1) - 1):
    #     for j in range(i+1, len(list1)):
    #         if list1[i] + list1[j] == target:
    #             print(f'index are{[i, j]}')
    list1 = gather_user()
    print('What will be the target? ')
    target = int(input('Target: '))
    dic_h = {}

    for idx, n in enumerate(list1):
        if (target - n) in dic_h:
            print([dic_h[target-n], idx]) 
        else:
            dic_h[n] =idx
        
            
main()