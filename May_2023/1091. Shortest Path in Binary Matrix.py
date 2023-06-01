class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        
        n = len(grid)

        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        direction=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        
        q=deque([(0,0,1)])
        
        while q:
            
            x,y,no_cell=q.popleft()
            
            if x==n-1 and y==n-1:
                return no_cell

            for d in direction:
                nx=x+d[0]
                ny=y+d[1]
                
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                   
                    
                    grid[nx][ny]=1
                    q.append((nx,ny,no_cell+1))
        return -1
