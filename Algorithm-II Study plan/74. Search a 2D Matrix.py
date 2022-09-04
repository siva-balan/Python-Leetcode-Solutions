class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        xrow =0
    
        if target >matrix[rows-1][0]:
                xrow +=rows-1
        else:      
            for i in range(rows):
                if target == matrix[i][0]:
                    return True

                if target< matrix[i][0]:
                    xrow += i-1
                    break
        for j in range(cols):
            if target == matrix[xrow][j]:
                return True
        return False
