class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        val = sum(k for k in nums if k%2 ==0)
        output = []
        n = len(nums)
        for i in range(len(queries)):
            x = queries[i][1]
            
            if nums[x]%2 ==0: val -= nums[x]
            nums[x] += queries[i][0]
            if nums[x]%2 == 0 : val += nums[x]
            output.append(val)
        return output
