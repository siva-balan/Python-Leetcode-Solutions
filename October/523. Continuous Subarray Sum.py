class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        d = {0:-1}
        s = 0
        for i,val in enumerate(nums):
            s += val
            rem = s % k
            
            if rem not in d:
                d[rem] = i
            elif i - d[rem] >1:
                return True
        return False
