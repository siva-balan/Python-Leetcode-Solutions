
# WORKING SOLUTION BUT TIME LIMIT EXCEEDED, BETTER SOLUTION IS BELOW THIS 

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        n = len(arr)
        
        if k >= n:
            return arr
        l,r = 0,k
        diff = inf
        output = arr[n-k:n]
        while r <= n:
            y = arr[l:r]
            d = 0
            for i in range(k):
                d += abs(x - y[i])
            if diff == d:
                output = min(y,output)
                r+=1
                l+=1
                continue
            diff = min(diff,d)
            output = y if diff == d else output
            l +=1
            r+=1
        return output
