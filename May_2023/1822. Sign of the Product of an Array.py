class Solution:
    def arraySign(self, nums: List[int]) -> int:

        output = nums[0]

        for i in range(1,len(nums)):
            output*= nums[i]
        
        if output == 0:
            return 0
        elif output >0:
            return 1
        else:
            return -1
