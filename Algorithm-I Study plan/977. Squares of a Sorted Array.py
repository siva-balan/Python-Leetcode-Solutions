class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n =0
        m = len(nums)-1
        arr = [0]*len(nums)
        x = len(nums)-1
        while m >= n and x>=0:
            if abs(nums[n])<= abs(nums[m]):
                arr[x] = nums[m]**2
                m -=1
            else:
                arr[x] = nums[n]**2
                n +=1
            x -=1
        return arr
