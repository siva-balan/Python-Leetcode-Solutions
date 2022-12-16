class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        """s = text1 if len(text1) <= len(text2) else text2
        output = 0

        if s == text1:
            x = 0
            while x != len(text1):
                for i in range()
                    if s[x] == i:
                        output += 1
                        x +=1
        else:
            x = 0
            for i in text1:
                if s[x] == i:
                    output += 1
                    x +=1

        return output"""
        m = len(text1)
        n = len(text2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[m][n] 
