class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum =nums[0]
        ans =nums[0]
        
        for i in range(1,len(nums)):
            sum = max(nums[i],sum+nums[i])
            ans = max(ans,sum)
        return ans
