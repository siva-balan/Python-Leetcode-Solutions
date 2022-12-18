class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        """output = []
        n = len(temperatures)
        for i in range(n):
            x = 0
            for j in range(i+1,n):
                if temperatures[j] > temperatures[i]:
                    output.append(j-i)
                    break
                else:
                    x += 1
                if x == n-i-1:
                    output.append(0)
        output.append(0)

        
        return output"""

        stack=[0]
        ans = [0]*len(temperatures)
        for i in range(1,len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]]  = i-stack[-1]
                stack.pop()
            stack.append(i)

        

        return ans
