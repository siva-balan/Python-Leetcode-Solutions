class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        r = len(grid)
        c = len(grid[0])
        area = 0
        #visited = [[0 for _ in range(c)]for _ in range(r)]
        
        def dfs(r1,c1):

            if r1 < 0 or c1 < 0 or r1 >= r or c1 >= c or grid[r1][c1] == 0:
                return 0
            grid[r1][c1] = 0
            
            return 1 + dfs(r1+1,c1) + dfs(r1-1,c1) + dfs(r1,c1+1) + dfs(r1,c1-1)    
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    area = max(dfs(i,j),area)
        
        return area
