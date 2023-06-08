class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        output = 0
        m,n = len(grid),len(grid[0])

        for i in range(m):
            l,r = 0,n
            while l < r:
                mid = (l+r)//2
                if grid[i][mid] >=0:
                    l = mid +1
                elif grid[i][mid] < 0:
                    r = mid
            output += (n - r)
        return output
