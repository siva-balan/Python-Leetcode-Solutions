class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr, nums):
            if( len(curr) >= 2 and curr[-1] < curr[-2] ): return
            if( len(curr) >= 2 and curr[:] not in result):
                result.add(curr[:])
            for i in range(len(nums)):
                backtrack( curr + (nums[i],), nums[i+1:] )
        result = set()
        backtrack( (), nums)
        return result
