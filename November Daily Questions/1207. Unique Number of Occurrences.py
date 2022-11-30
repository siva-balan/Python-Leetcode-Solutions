class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        d = {}

        for i in arr:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        
        x = list(d.values())
        x.sort()

        for j in range(1,len(x)):
            if x[j] == x[j-1]:
                return False
        
        return True
