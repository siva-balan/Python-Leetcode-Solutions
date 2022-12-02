class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = {}
        d2 = {}

        for i in word1:
            if i not in d1:
                d1[i] =1
            else:
                d1[i] +=1
        
        for j in word2:
            if j not in d2:
                d2[j] =1
            else:
                d2[j] +=1
        k1 = list(d1.keys())
        k2 = list(d2.keys())
        k11 = sorted(k1)
        k22 = sorted(k2)
        x = list(d1.values())
        y = list(d2.values())
        a = sorted(x)
        b =sorted(y)
        if a==b and k11 == k22:
            return True
        else:
            return False
