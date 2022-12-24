class Solution:
    def numTilings(self, n: int) -> int:

        queue = deque([0,1,2,5])
        if n < 4: 
            return queue[n]
        for i in range(n - 3):
            queue.popleft()
            queue.append(queue[0] + 2 * queue[-1])
        return queue[-1] % 1_000_000_007
