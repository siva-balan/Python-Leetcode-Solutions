class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        output = set(i for i in range(n))

        for i,j in  edges:
            if j in output:
                output.remove(j)
        
        return list(output)
