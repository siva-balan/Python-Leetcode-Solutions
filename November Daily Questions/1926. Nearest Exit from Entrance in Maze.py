class Solution:

    def isValid(self, maze, i, j):
        if i < 0 or i >= len(maze) or j < 0 or j >= len(maze[i]) or maze[i][j] == '+':
            return False
        return True

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        m = len(maze)
        n = len(maze[0])       
        
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = "+"
        
        row = [0, 1, 0, -1]
        col = [1, 0, -1, 0]
        while q:
            i, j, k = q.popleft()
            
            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c
                
                if self.isValid(maze, nRow, nCol):
                    if nRow == 0 or nRow == m-1 or nCol == 0 or nCol == n-1:
                        return k+1
                    
                    maze[nRow][nCol] = "+"
                    q.append((nRow, nCol, k+1))
        
        return -1
