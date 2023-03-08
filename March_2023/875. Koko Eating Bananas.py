class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1,max(piles)

        while l <r:
            m = (l+r)//2
            time = 0
            for i in piles:
                time += ceil(i/m)
            if time > h:
                l = m+1
            elif time <= h:
                r = m
        return r

