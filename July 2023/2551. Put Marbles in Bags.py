class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        n = len(weights)

        if n <= 2 or n==k:
            return 0

        output = [0]*(n-1)

        for i in range(n-1):
            output[i] = weights[i] + weights[i+1]

        output.sort()

        maxval = sum(output[n-k:])
        minval = sum(output[:k-1])

        return maxval-minval
