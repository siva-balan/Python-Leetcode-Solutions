class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        output = 0
        d = defaultdict(int)

        for row in grid:
            d[str(row)] +=1

        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            output += d[str(col)]
        
        return output
