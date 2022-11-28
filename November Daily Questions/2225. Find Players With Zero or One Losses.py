class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        d = {}

        for i in matches:
            if i[0] not in d:
                d[i[0]] = 0
            if i[1] not in d:
                d[i[1]] = 0
        
        for j in matches:
            if j[1] in d:
                d[j[1]] += 1
        out1 = []
        out2 = []
        for k,v in d.items():
            if v == 0:
                out1.append(k)
            if v == 1:
                out2.append(k)
        
        out1.sort()
        out2.sort()
        return [out1,out2]
