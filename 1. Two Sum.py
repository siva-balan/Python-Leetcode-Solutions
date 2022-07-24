class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i] + nums[j]:
                    return [i,j]
           
# optimized solution
    
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        s = {}
        for j in range(len(nums)):
            if target - nums[j] in s:
                return [j,s[target - nums[j]]]
            s[nums[j]] = j 
    
# Runtime: 83 ms, faster than 75.87% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 50.46% of Python3 online submissions for Two Sum.
