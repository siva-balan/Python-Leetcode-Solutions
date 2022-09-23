class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        res = ""
        for i in range(1,n+1):
            res += bin(i)[2:]
        
        res 
        return int(res,2) % (1000000000+7)
