class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
       
        count = 0
        l,pro = 0,1

        if k <=1:
            return 0

        for r,val in enumerate(nums):
            pro *= val
            while pro>=k:
                pro/= nums[l]
                l+=1
            count += r-l+1
        return count
