class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n = len(days)
        dp = [float('inf')] * 366
        dp[0] = 0
        j = 0
        for i in range(1, 366):
            if j < n and i == days[j]:
                dp[i] = min(dp[i], dp[i-1] + costs[0])
                if i >= 7:
                    dp[i] = min(dp[i], dp[i-7] + costs[1])
                else:
                    dp[i] = min(dp[i], costs[1])
                if i >= 30:
                    dp[i] = min(dp[i], dp[i-30] + costs[2])
                else:
                    dp[i] = min(dp[i], costs[2])
                j += 1
            else:
                dp[i] = dp[i-1]
        return dp[365]
