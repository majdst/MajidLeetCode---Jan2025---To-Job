class Solution:
    def twoSum(self, nums:list[int], target: int)->list[int]:


        m = len(nums)
        for i in range(m-1):
            for j in range(i+1, m):

                sum = nums[i]+nums[j]
                if sum == target:
                    return [i,j]
            
        



numx = [2, 11, 15, 5,  7]
targ = 9
solution = Solution()
print(solution.twoSum(numx, targ))