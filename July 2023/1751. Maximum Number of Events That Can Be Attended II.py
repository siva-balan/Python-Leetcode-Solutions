class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        #Sol from leetcode solutions

        events.sort()
        
        dp = {}
        def dfs(i, k, endTime):
            if i >= len(events) or k == 0:
                return 0

            if (i,k,endTime) in dp:
                return dp[(i,k,endTime)]

            res = 0
            if events[i][0] > endTime:
                res = dfs(i+1, k-1, events[i][1]) + events[i][2]
            
            res = max(res, dfs(i+1,k, endTime))
            dp[(i,k,endTime)] = res
            return res
        
        return dfs(0,k,-1)
