class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        output = 0
        diff = float("inf")
        total = sum(nums)
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            total -=nums[i]
            x = curr//(i+1)
            y = total//(len(nums)-i-1) if len(nums)-i-1 > 0 else 0
            if abs(x-y) >= diff:
                continue
            elif abs(x-y) < diff:
                diff = abs(x-y)
                output = i

        return output
