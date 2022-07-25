class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        s = {}
        for j in range(len(nums)):
            if target - nums[j] in s:
                return [j,s[target - nums[j]]]
            s[nums[j]] = j
