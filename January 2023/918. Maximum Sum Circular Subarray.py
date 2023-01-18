class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        #kadane algo : O(N2)
        """n= len(nums)
        finalout = float("-inf")
        for i in range(len(nums)):
            x,y = 0,float("-inf")
            for j in range(i,len(nums)+i):
                j = j%n
                x += nums[j]
                y = x if y < x else y
                x = 0 if x < 0 else x
            finalout = max(y,finalout)
        return finalout"""
        
        #O(N) solution
        n = len(nums)
        curr_max,totalmax = nums[0],nums[0]
        curr_min,totalmin = nums[0],nums[0]

        totalsum = sum(nums)
        for i in range(1,n):
            # Kadane's Algorithm to find Maximum subarray sum.
            curr_max = max(nums[i],nums[i]+curr_max)
            totalmax = max(totalmax,curr_max)

            # Kadane's Algorithm to find Minimum subarray sum.
            curr_min = min(nums[i],nums[i]+curr_min)
            totalmin = min(totalmin,curr_min)

        if totalmin == totalsum:
            return totalmax
        else:
            return max(totalmax,totalsum-totalmin)
