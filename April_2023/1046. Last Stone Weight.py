class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # stones.sort()

        # while len(stones) >1:
        #     y = stones.pop()
        #     x = stones.pop()

        #     if x != y:
        #         stones.append(y-x)
        #         stones.sort()
        # return stones[0] if len(stones) > 0 else 0
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) > 1:
            y = -(heappop(stones))
            x = -(heappop(stones))

            if x != y:
                heappush(stones,-(y-x))
            
        return - stones[0] if len(stones) > 0 else 0
