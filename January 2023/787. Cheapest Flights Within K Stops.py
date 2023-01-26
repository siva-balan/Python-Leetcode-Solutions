class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        d = defaultdict(list)
        for source, dest, price in flights:
            d[source].append([dest, price])

        cost_map = {src: 0} 
        queue = deque([(src, 0, 0)])
        while queue:
            city, cost_so_far, stops_taken = queue.popleft()
            for next_city, travel_cost in d[city]:
                if next_city not in cost_map or travel_cost + cost_so_far < cost_map[next_city]:
                    cost_map[next_city] = travel_cost + cost_so_far
                    if stops_taken < k:
                        queue.append((next_city, cost_map[next_city], stops_taken + 1))

        return cost_map[dst] if dst in cost_map else -1  
        """ d = defaultdict(list)
        
            for i in flights:
                d[i[0]].append((i[1],i[2]))
            output = [float("inf")]
            
            def bfs(q,count,dist):
                if count > k+1 or q is None:
                    return
                if q == dst:
                    output[0] = min(output[0],dist)
                else:
                    for i in d[q]:
                        bfs(i[0],count+1,dist+i[1])
            
            bfs(src,0,0)
            return output[0] if output[0] != float("inf") else -1"""
        
        
