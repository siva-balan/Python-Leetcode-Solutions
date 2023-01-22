class Solution:
    def ispal(self,y):
        return y == y[::-1]
    

    def backtracking(self,s,pal,output):
        if not s:
            output.append(pal)
        
        for i in range(1,len(s)+1):
            if self.ispal(s[:i]):
                self.backtracking(s[i:],pal + [s[:i]],output)

    def partition(self, s: str) -> List[List[str]]:

        output = []
        self.backtracking(s,[],output)
        return output
        
