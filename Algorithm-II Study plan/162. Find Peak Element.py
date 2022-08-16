class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) >= 2:
            if nums[0] > nums[1]:
                return 0
            elif nums[-1] > nums[-2]:
                return len(nums)-1
        l,r = 0, len(nums)-1
        
        while l <= r:
            m = (l+r)//2
            
            if m == 0 or nums[m] > nums[m+1] and nums[m]  > nums[m-1]:
                return m
            
            if nums[m] < nums[m-1] and m >0:
                r = m
            elif nums[m+1]> nums[m] and m < len(nums)-1:
                l = m+1
