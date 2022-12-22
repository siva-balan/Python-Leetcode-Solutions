class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = collections.defaultdict(list)
    
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        distance_data = {i:[1, 0] for i in range(n)}
        def compute_distance_data(node, prev_node):
            for child in graph[node]:
                if  child != prev_node:
                    compute_distance_data(child, node)
                    distance_data[node][0] += distance_data[child][0]
                    distance_data[node][1] += (distance_data[child][0] + distance_data[child][1])
    
        def compute_sum_of_distances(node, prev_node):
            for child in graph[node]:
                if child != prev_node:
                    distance_data[child][1] = distance_data[node][1] - distance_data[child][0] + (n-distance_data[child][0])
                    compute_sum_of_distances(child, node)
    
        compute_distance_data(0, -1)
        compute_sum_of_distances(0, -1)
    
        result = []
        for node in distance_data:
            result.append(distance_data[node][1])
    
        return result
