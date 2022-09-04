class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while n >=1:
            
            if nums.count(nums[i]) ==1:
                return nums[i]
            else:
                x = nums[i]
                print(x)
                nums.remove(x)
                nums.remove(x)
                n -=2
