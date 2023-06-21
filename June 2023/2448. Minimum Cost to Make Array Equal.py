class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        # output = float("inf")
        # n = len(nums)
        # for i in range(n):
        #     tcost = 0
        #     for j in range(n):
        #         if nums[j] != nums[i]:
        #             tcost += (abs(nums[j]-nums[i]))*cost[j]
        #     output = min(output,tcost)
        
        # return output

        # Solution from leetcode

        arr = sorted(zip(nums, cost))
        total, cnt = sum(cost), 0
        for num, c in arr:
            cnt += c
            if cnt > total // 2:
                target = num
                break
        return sum(c * abs(num - target) for num, c in arr)
