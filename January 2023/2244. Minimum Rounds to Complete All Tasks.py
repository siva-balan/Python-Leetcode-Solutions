class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        d = {}

        for i in tasks:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        output = 0
        
        for i in list(d.values()):
            if i == 1:
                return -1
            else:
                div = i//3
                if i% 3 == 0:
                    output += div
                else:
                    output += div +1
        return output
