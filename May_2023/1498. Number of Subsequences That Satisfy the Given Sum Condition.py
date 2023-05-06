class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()
        output = 0

        l,r = 0,len(nums)-1

        while l <= r:
            if nums[l] + nums[r] <= target:
                output += 2**(r-l)
                l +=1
            else:
                r -=1
        return output % (10**9+7)
