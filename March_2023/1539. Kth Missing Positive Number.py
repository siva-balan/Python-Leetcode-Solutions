class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        output = []

        i = 1
        while len(output) != k:
            if i not in arr:
                output.append(i)
            i+=1
        
        return output[k-1]
