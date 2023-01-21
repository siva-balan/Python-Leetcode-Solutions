# Solution from Neetcode

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        output = []

        def backtracking(i, dots, ip):
            if dots == 4 and i == len(s):
                output.append(ip[:-1])
                return
            if dots > 4:
                return 
            
            for j in range(i, min(i+3,len(s))):
                if int(s[i:j+1]) <= 255 and (s[i] != "0" or i == j):
                    backtracking(j+1,dots +1, ip + s[i:j+1] + ".")
        backtracking(0,0,"")

        return output
