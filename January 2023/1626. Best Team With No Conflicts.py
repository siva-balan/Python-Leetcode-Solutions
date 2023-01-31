class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        x = list(zip(ages,scores))

        x.sort(key = lambda x : (-x[0],-x[1]))
        """print(x)
        for i in range(len(x)):
            age,score = x[i][0] , x[i][1]
            total = x[i][1]
            for j in range(i+1,len(x)):
                if x[j][1] >= score:
                    score = x[j][1]
                    total += x[j][1]
            output = max(output,total)"""
    
        dp = [0] * len(x)

        for i in range(len(x)):
            dp[i] = x[i][1]
            for j in range(i):
                if x[j][1] >= x[i][1]:
                    dp[i] = max(dp[i],dp[j] + x[i][1])

        return max(dp)


