class Solution:
    def removeStars(self, s: str) -> str:

        no = s.count("*")
        i = 0
        while no >0 and i >= 0:
            if s[i] == "*":
                s = s[:i-1] + s[i+1:]
                i -=1
                no -=1
            else:
                i+=1
        return s
