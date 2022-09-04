# Done using Dynamic programming
#Runtime: 699 ms, faster than 88.85% of Python3 online submissions for 01 Matrix.
#Memory Usage: 17.2 MB, less than 58.29% of Python3 online submissions for 01 Matrix.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        x = math.inf
        ans  = [[2 for _ in range(n)]for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                val1,val2 = x,x
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    continue
                if 0<= i-1 < m: 
                    val1 = ans[i-1][j]
                if 0<= j-1 < n:
                    val2 = ans[i][j-1]
                ans[i][j] = 1+ min(val1,val2)
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                val1,val2 = x,x
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    continue
                if 0<= i+1 < m: 
                    val1 = ans[i+1][j]
                if 0<= j+1 < n:
                    val2 = ans[i][j+1]
                ans[i][j] =min((1+min(val1,val2)), ans[i][j])
        
        
        return ans
