class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=0
        for i in range(len(nums)):
            if i<=len(nums)-2 and nums[i]==nums[i+1]:
                continue
            nums[n]=nums[i]
            n+=1
        return n
