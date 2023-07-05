class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        l,zero,output = 0,0,0

        for r in range(n):
            if nums[r] == 0:
                zero +=1
            
            while zero > 1:
                if nums[l] == 0:
                    zero -=1
                l +=1
            
            output = max(output,r-l+1-zero)
        
        if output == n:
            return output -1
        else:
            return output
