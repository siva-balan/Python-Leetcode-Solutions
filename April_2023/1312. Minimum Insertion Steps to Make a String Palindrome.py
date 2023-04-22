class Solution:
    def minInsertions(self, s: str) -> int:

        @lru_cache(None)

        def dp(i,j):
            if i == j:
                return 1
            elif i > j:
                return 0

            if arr[i] == arr[j]:
                val = 2 + dp(i+1,j-1)
                return val
            else:
                val = max(dp(i+1,j),dp(i,j-1))
                return val
        
        arr = list(s)

        x = dp(0,len(arr)-1)

        return len(s) - x
