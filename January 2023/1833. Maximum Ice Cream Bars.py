class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()
        output = 0
        for i in costs:
            if coins -i >=0:
                output +=1
                coins -=i
        return output
