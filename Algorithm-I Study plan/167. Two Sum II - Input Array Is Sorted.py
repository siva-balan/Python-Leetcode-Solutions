class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers) -1
        arr =[]
        while i<j :
            if numbers[i] + numbers[j] == target:
                arr.append(i+1)
                arr.append(j+1)
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -=1
        return arr

    # optimized solution
    
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        s = {}
        for j in range(len(nums)):
            if target - nums[j] in s:
                return [j,s[target - nums[j]]]
            s[nums[j]] = j 
    
# Runtime: 83 ms, faster than 75.87% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 50.46% of Python3 online submissions for Two Sum.
