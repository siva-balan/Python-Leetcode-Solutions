class Solution:
    def dices(self,k,rem,dice,ways):
            if rem <=0 or rem > dice*k:
                return 0
            if dice == 1 and rem <=k:
                return 1
            
            if (rem,dice) not in ways:
                x = 0
                for i in range(1,k+1):
                    x += (self.dices(k,rem-i,dice-1,ways))
                ways[(rem,dice)] = x
            return ways[(rem,dice)]
        
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        return self.dices(k,target,n,{}) % ((10**9) +7)
    
