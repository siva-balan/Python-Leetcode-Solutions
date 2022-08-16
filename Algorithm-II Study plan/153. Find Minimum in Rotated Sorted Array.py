class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        res = math.inf
        while l <=r:
            m = (l+r)//2
            
            if nums[l] < nums[r]:
                return min(res,nums[l])
            
            if nums[m] >= nums[l]:
                l = m+1
                res = min(res,nums[m])
            else:
                r = m-1
                res = min(res,nums[m])
        return res
