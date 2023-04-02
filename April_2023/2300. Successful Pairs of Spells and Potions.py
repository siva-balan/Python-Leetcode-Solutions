class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()

        pairs = []

        for i in range(len(spells)):
            # for j in range(len(potions)):
            #     if spells[i]*potions[j] >= success:
            #         pairs.append(len(potions)-j)
            #         break
            #     elif j == len(potions)-1:
            #         pairs.append(0)
            l,r = 0 ,len(potions) -1
            index = -1
            while l <=r:
                m = (l+r)//2
                if spells[i]*potions[m] >= success:
                    index = m
                    r = m-1
                else:
                    l = m+1
            if index == -1: pairs.append(0)
            else: pairs.append(len(potions)-index)
        return pairs
