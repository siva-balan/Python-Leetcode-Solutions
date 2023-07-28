class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        # self.output = False
        # def game(p1,p2,arr,flag):
        #     if len(arr) == 0:
        #         if p1>= p2:
        #             self.output = True
        #         return
        #     if flag:
        #         game(p1+arr[0],p2,arr[1:],False)
        #         game(p1+arr[len(arr)-1],p2,arr[:len(arr)-1],False)
        #     else:
        #         game(p1,p2+arr[0],arr[1:],True)
        #         game(p1,p2+arr[len(arr)-1],arr[:len(arr)-1],True)

        # game(0,0,nums,True)
        # return self.output

        n = len(nums)
        dp = nums[:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0
