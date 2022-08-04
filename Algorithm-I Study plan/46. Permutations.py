class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutes = []
        
        def backtracking(currpermute,nums):
            if len(nums) == 0 :
                permutes.append(currpermute)
            
            
            for i in range(len(nums)):
                
                backtracking(currpermute + [nums[i]],nums[:i] + nums[i+1:])
        
        backtracking([],nums)
        return permutes
