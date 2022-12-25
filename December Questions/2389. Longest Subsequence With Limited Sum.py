class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        """nums.sort()
        output = []
        for i in range(len(queries)):
            l, r = 0, len(nums)-1
            x = 0
            while queries[i] >= x and l < len(nums) and r >= 0 :
                if x == queries[i] or (x+ nums[r] > queries[i] and x + nums[l] > queries[i]):
                    break
                if x + nums[r] <= queries[i]:
                    x += nums[r]
                    r -= 1
                else:
                    x += nums[l]
                    l +=1
            output.append(len(nums) -r+l-1)
        return output"""

        nums.sort()
        answer = []
        for i in range(len(queries)):
            sum = 0
            count = 0
            for j in range(len(nums)):
                if sum+nums[j]<=queries[i]:
                    sum += nums[j]
                    count += 1
                else:
                    break
            answer.append(count)        
       
        return answer
