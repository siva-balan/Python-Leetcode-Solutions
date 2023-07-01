class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        #Sol from leetcode
        output = float('inf')
        distribution = [0] * k
        
        def backtrack(i):
            nonlocal output, distribution
            
            if i == len(cookies):
                output = min(output, max(distribution))
                return
            
            if output <= max(distribution):
                return
            
            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]
        
        backtrack(0)
        return output
