class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if haystack is None or needle is None:
            return -1
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            if needle == haystack[i:i+n]:
                return i
        return -1
        
