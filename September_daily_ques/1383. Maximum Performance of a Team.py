
# DATE: 11/9/22

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        
        team = []
        
        for eff,sp in zip(efficiency,speed):
            team.append([eff,sp])
        
        team.sort(reverse = True)
        minheap =[]
        res, speed = 0,0
        
        for eff,sp in team:
            if len(minheap) == k:
                speed -= heapq.heappop(minheap)
            speed += sp
            res = max(res,eff*speed)
            heapq.heappush(minheap,sp)
        
        return res % (10**9 +7)
