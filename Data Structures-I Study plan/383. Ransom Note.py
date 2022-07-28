class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = defaultdict(int)
        m = defaultdict(int)
        for i in ransomNote:
            if i in r:
                r[i] +=1
            else:
                r[i] = 1
        for i in magazine:
            if i in m:
                m[i] +=1
            else:
                m[i] = 1
        count = 0
        for i in r.keys():
            if r[i] <= m[i]:
                count +=1
            else:
                return False
        if count == len(r):
            return True
        
