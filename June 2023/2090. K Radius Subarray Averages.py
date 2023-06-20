class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        output = [-1]*n

        total,left = 0,0
        size = 0
        needed = (2*k) +1
        for i in range(n):
            total += nums[i]
            size +=1
            if size == needed:
                output[left+k] = int(total/needed)
                total -= nums[left]
                left +=1
                size -=1
        
        return output
