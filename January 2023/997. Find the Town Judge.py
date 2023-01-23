class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        d= defaultdict(list)
        d2 = defaultdict(list)
        for i in range(len(trust)):
            x = trust[i][0]
            y = trust[i][1]
            d[y].append(x)
            d2[x].append(y)
        for i in range(1,n+1):
            if len(d[i]) == n-1 and i not in d2:
                return i
        return -1
