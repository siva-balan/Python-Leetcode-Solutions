class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        output = [[0 for _ in range(n)] for _ in range(n)]

        l,r = 0, n
        t,b = 0,n
        val = 1
        while l < r and t < b:

            for i in range(l,r):
                output[t][i] = val
                val +=1
            t +=1

            for i in range(t,b):
                output[i][r-1] = val
                val +=1
            r -=1

            if not(l<r and t <b):
                break
            
            for i in range(r-1,l-1,-1):
                output[b-1][i] = val
                val+=1
            b -=1

            for i in range(b-1,t-1,-1):
                output[i][l] = val
                val +=1
            l +=1
        
        return output
