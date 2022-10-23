class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums.sort()
        dup = 0
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                dup = nums[i]
        s =set(nums)
        
        for i in range(1,n+1):
            if i not in s:
                return [dup,i]
