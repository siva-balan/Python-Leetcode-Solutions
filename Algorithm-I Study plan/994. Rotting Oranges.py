class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time, fresh = 0,0
        
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    queue.append([r,c])
        
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue and fresh >0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for cr,cc in directions:
                    row,col = r+ cr, c+ cc # moving in four directions
                    if 0<=row<rows and 0<=col <cols and grid[row][col] ==1:
                        grid[row][col] = 2
                        fresh -=1
                        queue.append([row,col])
            time +=1
        
        if fresh == 0:
            return time
        else: return -1
                    
