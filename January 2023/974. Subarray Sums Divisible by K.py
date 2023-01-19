class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        """output = 0
        total = sum(nums)
        for i in range(len(nums)):
            if i >0:
                total -= nums[i-1]
            x  = total
            if total % k == 0:
                output +=1
            for j in range(len(nums)-1,i,-1):
                x -= nums[j]
                if x % k == 0:
                    output +=1
        return output"""

        output = 0
        currsum = 0
        d = defaultdict(int)
        d[0] =1
        for n in nums:
            currsum +=n
            output += d[currsum%k]
            d[currsum%k] +=1
        
        return output
