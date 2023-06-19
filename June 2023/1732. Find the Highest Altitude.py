class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        output = 0
        al = 0

        for i in range(len(gain)):
            al += gain[i]
            output = max(output,al)
        
        return output
