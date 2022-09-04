class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        d = defaultdict(int)
        if len(n) == 1 and int(n) ==1:
            return True   
        
        while len(n) >= 1 and d[int(n)] <= 1:
            s = 0
            for i in range(len(n)):
                s += int(n[i])**2
            d[s] +=1
            if s == 1 and d[s] == 1:
                return True
            n = str(s) 
        return False
