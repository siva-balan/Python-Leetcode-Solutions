class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        # nums.sort()
        # output = 0
        # print(nums)
        # while p > 0:
        #     val = min((nums[1]-nums[0]),(nums[-1]-nums[-2]))
        #     if val == nums[1] - nums[0]:
        #         nums.pop(0)
        #         nums.pop(0)
        #     else:
        #         nums.pop()
        #         nums.pop()

        #     output = max(output,val)
        #     print(val,output)
        #     p -=1
        
        # return output

        nums.sort()

        def isFeasible(diff):
            count = 0
            i = 0
            while i < len(nums) - 1 and count < p:
                if nums[i+1] - nums[i] <= diff:
                    count += 1
                    i += 2
                else:
                    i += 1
            
            return count >= p

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid_diff = (left + right) // 2
            if isFeasible(mid_diff):
                right = mid_diff
            else:
                left = mid_diff + 1
        
        return left
