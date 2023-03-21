class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        # output = 0

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         for j in range(i,len(nums)):
        #             if nums[j] != 0:
        #                 output += j-i
        #                 break
        #             elif nums[j] == 0  and j == len(nums)-1:
        #                 output += j-i+1
        #                 break
        # return output

        total = current = 0
                
        for num in nums:
            if num == 0:
                current += 1
                total += current
            else:
                current = 0
                
        return total
