class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = {}
        
        for i in words:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        l = []
        for key,values in d.items():
            l.append([key,values])
        
        l.sort(key = lambda x : (-x[1],x[0]))
        output = []
        i = 0
        while k > 0:
            output.append(l[i][0])
            i +=1
            k -=1
        return output
