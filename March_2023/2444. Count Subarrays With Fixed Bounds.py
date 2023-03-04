class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        n = len(nums)
        leftBound = -1
        lastMin, lastMax = -1, -1
        count = 0
        
        for i in range(n):
            if nums[i] >= minK and nums[i] <= maxK:
                if nums[i] == minK:
                    lastMin = i 
                if nums[i] == maxK:
                    lastMax = i 
                count += max(0, min(lastMin, lastMax) - leftBound)
            else:
                leftBound = i
                lastMin = -1
                lastMax = -1
        
        return count
