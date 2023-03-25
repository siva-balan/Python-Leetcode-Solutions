class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        paths = defaultdict(dict)
        for x,y in connections:
            paths[x][y] = 1 
            paths[y][x] = 0 
            
        visited = set()
        result = 0
        def dfs(current_city):
            nonlocal result
            visited.add(current_city)
            total = 0
            for next_city in paths[current_city]:
                if next_city not in visited:
                    fix = paths[current_city][next_city]
                    result += fix
                    dfs(next_city)

        dfs(0)
        return result
