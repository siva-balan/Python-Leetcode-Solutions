class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        """output = [float("inf")]
        m = len(grid)
        n = len(grid[0])
        def back(val,i,j):
            if i == m-1 and j == n-1:
                output[0] = min(output[0],val)
                return
            if val >= output[0]:
                return
            if i+1 < m:
                back(val+grid[i][j],i+1,j)
            if j+1 <n:
                back(val+grid[i][j],i,j+1)
            return
        
        back(0,0,0)
        return output[0]"""

        row = len(grid)
        col = len(grid[0])
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
        for j in range(1, col):
            grid[0][j] += grid[0][j-1]
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[row-1][col-1]
