class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        d = {}

        for i in range(len(order)):
            d[order[i]] = i

        for i in range(1,len(words)):
            f,s = words[i-1], words[i]
            n = min(len(f),len(s))
            flag = 0
            for j in range(n):
                if d[f[j]] > d[s[j]]:
                    return False
                elif d[f[j]] < d[s[j]]:
                    flag = 1
                    break
            if flag == 0 and len(f) > len(s):
                return False
        return True
