class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        x =s
        if k == 1:
            for i in range(len(s)):
                x = min(x,s[i:] + s[:i] )
            return x
        return "".join(sorted(s))
