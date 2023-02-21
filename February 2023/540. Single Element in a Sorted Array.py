class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        """ n = len(nums)
        l,r = 0,n-1
        if len(nums) == 1: return nums[0]
        while l <=r:
            m = (l+r)//2
            if (m-l)%2 == 0 and (r-m)%2==0:
                if m>0 and m <r:
                    if nums[m-1] == nums[m]:
                        r = m
                    elif nums[m+1] == nums[m]:
                        l = m
                    else:
                        return nums[m]
            else:
                if m>0 and m <r:
                    if nums[m-1] == nums[m]:
                        l = m
                    elif nums[m+1] == nums[m]:
                        r = m
                    else:
                        return nums[m]"""
        
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                r = mid
            else:
                l = mid + 2
        return nums[l]
