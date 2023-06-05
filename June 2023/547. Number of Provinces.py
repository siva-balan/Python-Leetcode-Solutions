class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        visited = [False]* n
        output = 0

        def check(node):
            visited[node] = True

            for i in range(n):
                if isConnected[node][i] == 1 and not visited[i]:
                    check(i)
        
        for i in range(n):
            if not visited[i]:
                output +=1
                check(i)

        return output
        
