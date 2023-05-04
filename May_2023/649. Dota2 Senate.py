class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        rad, di = [], []
        n = len(senate) -1
        for i in range(len(senate)):
            if senate[i] == "R":
                rad.append(i)
            else:
                di.append(i)
            
        while len(rad) > 0 and len(di)> 0:
            if rad[0] > di[0]:
                di.pop(0)
                rad.pop(0)
                n +=1
                di.append(n)
            else:
                di.pop(0)
                rad.pop(0)
                n +=1
                rad.append(n)

        if len(rad)> 0: return "Radiant"
        else: return "Dire"
