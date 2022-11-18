class Solution:
    def isUgly(self, n: int) -> bool:
        
        fac = [2,3,5]
        if n==0: return False
        if n == 1:
            return True
        for i in fac:
            while n%i == 0:
                n /= i
        return True if n==1 else False
