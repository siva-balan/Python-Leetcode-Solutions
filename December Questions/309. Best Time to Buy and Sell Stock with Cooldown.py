class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # neet code solution
        # caching
        d = {}

        def dfs(i,buying):
            if i >= len(prices):
                return 0
            if (i,buying) in d:
                return d[(i,buying)]
            
            if buying:
                buy  = dfs(i+1,not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                d[(i,buying)] = max(buy,cooldown)
            else:
                sell = dfs(i+2, not buying)  + prices[i]
                cooldown = dfs(i+1, buying)
                d[(i,buying)] = max(sell,cooldown)
            return d[(i,buying)]
        return dfs(0,True)
