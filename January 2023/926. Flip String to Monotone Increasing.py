class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        zero = s.count("0")
        one = 0
        output = zero

        for i in s:
            if i == "0":
                zero -=1
            else:
                one +=1
            output = min(output,zero+one)
        return output
