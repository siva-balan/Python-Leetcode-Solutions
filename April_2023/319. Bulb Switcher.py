class Solution:
    def bulbSwitch(self, n: int) -> int:

        # bulb = ["off"]*n

        # for i in range(n):
        #     for j in range(i,n,i+1):
        #         if bulb[j] == "off":
        #             bulb[j] = "on"
        #         else:
        #             bulb[j] = "off"
        
        # return bulb.count("on")

        return floor(sqrt(n))
