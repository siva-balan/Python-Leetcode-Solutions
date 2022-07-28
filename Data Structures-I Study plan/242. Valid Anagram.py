class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        r = defaultdict(int)
        m = defaultdict(int)
        
        for i in s:
            r[i] +=1
        for i in t:
            m[i] +=1
        
        for x in r.keys():
            if r[x] == m[x]:
                continue
            else:
                return False
        return True
