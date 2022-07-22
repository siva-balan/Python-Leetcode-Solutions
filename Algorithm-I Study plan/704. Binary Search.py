class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = len(nums)//2
        
        left = 0
        right = len(nums) -1
        while left <= right:
            if target > nums[middle]:
                left = middle +1
                middle = (left + right)//2
            elif target < nums[middle]:
                right  = middle -1
                middle = (left + right)//2
            elif target == nums[middle]:
                return middle
        return -1
