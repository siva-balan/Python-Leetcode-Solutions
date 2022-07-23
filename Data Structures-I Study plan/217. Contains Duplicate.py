class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        if len(nums) == 1:
            return False
        if len(nums) == 2 and nums[0] == nums[1]:
            return True
            
        n = len(nums)-1
        for i in range(n):
            if nums[i] == nums[i+1]:
                return True
        return False
     
# Runtime: 629 ms, faster than 56.65% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26.1 MB, less than 5.09% of Python3 online submissions for Contains Duplicate.

# Optimized solution

from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = Counter(nums)
        
        for i in x:
            if x[i] >=2:
                return True
        return False
    
# Runtime: 616 ms, faster than 59.29% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 25.9 MB, less than 72.31% of Python3 online submissions for Contains Duplicate.
