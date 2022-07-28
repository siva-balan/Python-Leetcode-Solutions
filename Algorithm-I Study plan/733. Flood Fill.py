class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        current = image[sr][sc]
        rows =  len(image)
        col = len(image[0])
        
        
        def dfs(sr,sc):
            if 0<= sr < rows and 0 <= sc < col and image[sr][sc] != color and image[sr][sc] == current:
                image[sr][sc] = color
                
                dfs(sr+1,sc)
                dfs(sr-1,sc)
                dfs(sr,sc+1)
                dfs(sr,sc-1)
                
        dfs(sr,sc)
        
        return image
