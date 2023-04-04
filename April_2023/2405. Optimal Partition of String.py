class Solution:
    def partitionString(self, s: str) -> int:
        output = 0
        cut = 0
        for i in range(1,len(s)):
            if s[i] in s[cut:i]:
                output +=1
                cut = i
        return output +1
