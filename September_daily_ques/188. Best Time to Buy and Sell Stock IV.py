class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        min_p = [float("inf")] * (k + 1)
        max_profit = [0] * (k + 1)
        
        for price in prices:
            for i in range(1, k + 1):
                min_p[i] = min(min_p[i], price - max_profit[i-1])
                max_profit[i] = max(max_profit[i], price - min_p[i])

        return max_profit[k]
