class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        output = 0
        currsum = 0
        d = defaultdict(int)
        d[0] = 1

        for n in nums:
            currsum += n
            dif  = currsum - k
            output += d[dif]
            d[currsum] +=1
        return output
