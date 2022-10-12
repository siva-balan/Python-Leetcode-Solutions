class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        output = 0
        for i in range(len(nums)-2):
            if nums[i+1] + nums[i] > nums[i+2]:
                output = max(output,nums[i]+nums[i+1]+nums[i+2])
        return output                
