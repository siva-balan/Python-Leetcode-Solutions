import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        piles = [-i for i in piles]
        heapq.heapify(piles)

        while k >0:
            x = heapq.heappop(piles)//2
            heapq.heappush(piles,x)
            k -=1
        
        return -sum(piles)
