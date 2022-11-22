class Solution:
    def numSquares(self, n: int) -> int:

        sq = [x**2 for x in range(1,int(n**(1/2))+1)]
        dp = [1]*(n+1)
        dp[0] = 0

        for i in range(1,n+1):
            if i in sq:
                continue
            dp[i] = dp[i-1] +1
            for s in sq:
                if s >i:
                    break
                if dp[i] > dp[i-s]+1:
                    dp[i] = dp[i-s]+1
        return dp[-1]
