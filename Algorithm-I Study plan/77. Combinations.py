class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        l = [i+1 for i in range(n)]
        comb = combinations(l,k)
        return comb
      
      
 # backtracking soln


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
     
        res = []
        comb = []
        def backtracking(start,comb):
            if len(comb) == k:
                res.append(comb.copy())
            
            for i in range(start,n+1):
                comb.append(i)
                backtracking(i+1,comb)
                comb.pop()
                
        backtracking(1,comb)
        return res
