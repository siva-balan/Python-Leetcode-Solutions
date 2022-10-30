class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = collections.deque([])

        q.append((0, 0, 0, k))
        seen = set()
        while q:
            r, c, steps, rk = q.popleft()
			
            if r == rows-1 and c == cols - 1:
                return steps
            else:
                for y, x in directions:
                    nr = r + y
                    nc = c + x
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc, rk) not in seen:
                        if grid[nr][nc] == 1 and rk > 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk - 1))

                        elif grid[nr][nc] == 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk))

        return -1
