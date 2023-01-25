class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        """d = {}

        for i in range(len(edges)):
            if i not in d:
                if edges[i] != -1:
                    d[i] = edges[i] 
        print(d)
        path = []
        path1 = []
        while node1 in d:
            path.append(node1)
            node1 = d[node1] if node1 in d else None
        while node2 in d:
            path1.append(node2)
            node2 = d[node2] if node2 in d else None
        if len(path) < len(path1):
            path,path1 = path, path1
        output = float("inf")
        for i in range(len(path)):
            if path[i] in path1:
                for j in range(len(path1)):
                    if path[i] == path[j]:
                        output = min(i,j)
        
        return output if output != float("inf") else -1"""


        if node1 == node2: return node1
        seen1 = set()
        seen2 = set()
        while node1 not in seen1 or node2 not in seen2:
            seen1.add(node1)
            seen2.add(node2)
            if node1 != -1: 
                node1 = edges[node1]
            if node2 != -1: 
                node2 = edges[node2]
            if node1 != -1 and node1 == node2: return node1
            if node1 in seen2 and node1 != -1 and node2 in seen1 and node2 != -1:
                return min(node1, node2)
            if node1 in seen2 and node1 != -1:
                return node1
            if node2 in seen1 and node2 != -1:
                return node2
        return -1
