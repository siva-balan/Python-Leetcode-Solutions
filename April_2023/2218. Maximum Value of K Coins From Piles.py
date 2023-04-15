class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        pref = [[] for _ in range(n)]  
        for i in range(n):
            pref[i] = [0] * len(piles[i])  
            pref[i][0] = piles[i][0]  
            for j in range(1, len(piles[i])):
                pref[i][j] = pref[i][j - 1] + piles[i][j]

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for cur in range(len(piles[i - 1]) + 1):
                    if cur <= j:
                        if cur > 0:
                            dp[i][j] = max(dp[i][j], dp[i - 1][j - cur] + pref[i - 1][cur - 1])
                        else:
                            dp[i][j] = max(dp[i][j], dp[i - 1][j - cur])
        return dp[n][k]
