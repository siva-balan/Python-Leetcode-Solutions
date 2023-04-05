class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        #Soln from neetcode
        output = nums[0]
        total = nums[0]
        for i in range(1,len(nums)):
            total += nums[i]
            val = ceil(total/(i+1))
            output = max(output,val)
        
        return output
