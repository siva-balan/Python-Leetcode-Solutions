
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = -1
            else:
                d[s[i]]  = i
 
        for j in d.values():
            if j >= 0:
                return j
        return -1
