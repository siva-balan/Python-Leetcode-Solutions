class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        l,output = 0 ,math.inf
        sum = 0
        for i in range(n):
            sum += nums[i]
            while target <= sum:
                sum -= nums[l]
                output = min(output,i-l+1)
                l += 1
                
        return 0 if output == math.inf else output
