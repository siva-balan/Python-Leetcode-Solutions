class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        left = 0
        result = 0
        for i in range(len(s)):
            while s[i] in x:
                x.remove(s[left])
                left +=1
            x.add(s[i])
            result = max(result, i-left+1)
        return result
