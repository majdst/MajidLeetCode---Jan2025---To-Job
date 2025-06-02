nums = [2,7,11,15]
target = 9

def sum_two_if():

    for i in range(len(nums)):

        for j in range(i+1, len(nums)):

            if nums[i] + nums[j] == target:

                return i, j
    return None

def sum_two_dict():

    #Creating the dictionary
    num_dict = {}

    for i, numbers in enumerate(nums):

        x = target - numbers

        if x in num_dict:

            return i, num_dict[x]
        
        num_dict[numbers] = i

def main():

    print(sum_two_dict())


main()


