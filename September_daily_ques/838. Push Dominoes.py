class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        n = len(dominoes)
        dominoes = list(dominoes)
        q = []
        for i in range(n):
            if dominoes[i] != ".":
                q.append(i)
        
        while len(q) > 0:
            i = int(q.pop(0))
            if dominoes[i] == "R":
                if i+1 < n and dominoes[i+1] == ".":
                    if i+2 < n and dominoes[i+2] == "L":
                        q.pop(0)
                        continue
                    else:
                        dominoes[i+1] = "R"
                        q.append(i+1)
            if dominoes[i] == "L" and i-1 >= 0 and dominoes[i-1] == ".":
                        dominoes[i-1] = "L"
                        q.append(i-1) 
                
        return "".join(str(i) for i in dominoes)
