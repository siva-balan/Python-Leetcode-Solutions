class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        """output = [0]
        def words(i,w,k,l,visited):
            if word == w:
                output[0] +=1
                return
            if k >= len(board) or k <0 or l >= len(board[0]) or l <0 or i >= len(word):
                return
            
            if word[i] == board[k][l] and visited[k][l] is False:
                w += board[k][l]
                visited[k][l] = True
                words(i+1,w,k,l+1,visited)
                words(i+1,w,k,l-1,visited)
                words(i+1,w,k+1,l,visited)
                words(i+1,w,k-1,l,visited)
            return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visit = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                words(0,"",i,j,visit)
                if output[0] >=1:
                    return True
        return False"""

        rows = len(board)
        cols = len(board[0])
        
        
        
        def dfs(r, c, index):
            if index == len(word):
                return True 
            
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]
                or (r, c) in visited):
                return False
            
            visited.add((r, c))
            
            
            paths = [(r + 1, c), 
                    (r - 1, c),
                    (r, c + 1), 
                    (r, c - 1)]
            
            ans = False
            for row, col in paths:
                ans |= dfs(row, col, index + 1)
                
            visited.remove((r, c))
                
            return ans 
        
        for r in range(rows):
            for c in range(cols):
                visited = set()
                if dfs(r, c, 0):
                    return True
                    
        return False
