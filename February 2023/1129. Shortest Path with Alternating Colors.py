class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        """red,blue = defaultdict(list),defaultdict(list)
        for x,y in redEdges:
            red[x].append(y)
        for x,y in blueEdges:
            blue[x].append(y)
        output =  [-1]*n

        r,b = False,False
        def bfs(q,r,b,d,x):
            node = q
            if x == node:
                output[node] = d
            if node in red and r is False:
                for i in red[node]:
                    bfs(i,True,False,d+1,x+1)
            if node in blue and b is False:
                for j in blue[node]:
                    bfs(j,False,True,d+1,x+1)
            return
        bfs(0,r,b,0,0)

        return output"""

        R, B, Gray = 0, 1, 2
        G = defaultdict(list)
        for v, w in redEdges:
            G[v].append((w,R))
        for v, w in blueEdges:
            G[v].append((w,B))
        que = deque([(0,0,Gray)])
        visited = set()
        res = [-1]*n
        dist = defaultdict(int)
        while que:
            d, v, vcolor = que.popleft()
            if (v, vcolor) in visited: continue
            visited.add((v,vcolor))
            if v not in dist: dist[v] = d
            res[v] = dist[v]
            for w, color in G[v]:
                if vcolor != color:
                    que.append((d+1, w, color))
        return res
