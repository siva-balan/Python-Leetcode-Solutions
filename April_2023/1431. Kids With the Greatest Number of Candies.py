class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxval = max(candies)

        output = ["False"] * len(candies)

        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= maxval:
                output[i] = True
            else:
                output[i] = False
        
        return output
