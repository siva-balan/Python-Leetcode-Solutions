class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m  = len(mat)
        n = len(mat[0])
        
        if m*n != r*c: return mat
      
        output = [[0 for x in range(c)]for x in range(r)]
     
        x =0
        for i in range(m):
            for j in range(n):
                output[x//c][x%c] = mat[i][j]
                x +=1      
            
        return output
