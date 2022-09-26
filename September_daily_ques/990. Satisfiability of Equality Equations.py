class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = [i for i in range(26)]
        
        
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            else:
                return x
        def union(x,y):
            a = find(x)
            b = find(y)
            
            parent[b] = a
            
        for eq in equations:
            if eq[1] == "!":
                continue
            a1 = ord(eq[0]) - ord('a')
            b1 = ord(eq[3]) - ord('a')
            union(a1,b1)
        
        for eq in equations:
            if eq[1] != "!":
                continue
            a1 = ord(eq[0]) - ord('a')
            b1 = ord(eq[3]) - ord('a')
            
            if find(a1) == find(b1):
                return False
        return True
