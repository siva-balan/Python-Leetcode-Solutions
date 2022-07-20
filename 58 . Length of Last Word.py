class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        rev = s[::-1]
        rev = rev.lstrip()
        t = rev.split(" ",1)
        return len(t[0])
