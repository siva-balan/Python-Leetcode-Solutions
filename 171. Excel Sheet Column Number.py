class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        n = len(columnTitle)
        output = 0
        while n > 0:
            output += (26**(n-1))*(ord(columnTitle[len(columnTitle)-n]) - 64)
            n -=1
        return output
