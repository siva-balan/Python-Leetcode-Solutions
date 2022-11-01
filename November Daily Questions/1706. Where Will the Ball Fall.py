class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        r = len(grid)
        c = len(grid[0])
        output = []
        
        for y in range(c):
            col = y
            for x in range(r):
                nextcol = col + grid[x][col]
                
                if nextcol < 0 or nextcol >=c or grid[x][col] != grid[x][nextcol]:
                    col = -1
                    break
                col = nextcol
            output.append(col)
        return output
