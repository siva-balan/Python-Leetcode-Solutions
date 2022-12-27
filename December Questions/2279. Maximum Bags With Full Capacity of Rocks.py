class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        rem = []
        output = 0
        for i in range(len(rocks)):
            rem.append((capacity[i] - rocks[i]))
        
        rem.sort()

        for r in rem:
            if r == 0:
                output +=1
            elif additionalRocks -r >=0:
                additionalRocks -=r
                output +=1
        return output
