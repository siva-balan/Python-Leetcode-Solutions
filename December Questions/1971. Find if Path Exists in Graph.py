class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        visited = [False]*n

        d = {}

        for x in edges:
            k,v = x
            if k not in d:
                d[k] = [v]
            else:
                d[k].append(v)
            
            if v not in d:
                d[v] = [k]
            else:
                d[v].append(k)
        
        queue = [source]

        while queue:
            curr = queue.pop()

            if curr == destination:
                return True
            elif curr in d and not visited[curr]:
                queue.extend(d[curr])
            visited[curr] = True
        return False
