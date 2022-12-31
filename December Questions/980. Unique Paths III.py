class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])
        count = m*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: start = (i,j)
                if grid[i][j] == 2: end = (i,j)
                if grid[i][j]==-1: count -= 1
        
        self.ans = 0
        def backtrack(i,j,path):
            if path[-1]==end:
                if len(path)==count: self.ans+=1
                return
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<m and 0<=y<n and grid[x][y] != -1 and (x,y) not in path:
                    backtrack(x,y,path + [(x,y)])
        backtrack(start[0],start[1],[start])
        return self.ans
      
      # solution written using leetcode discussions
