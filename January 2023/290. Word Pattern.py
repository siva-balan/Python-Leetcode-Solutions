class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        word = s.split(" ")

        if len(word) != len(pattern):
            return False
        
        d = {}

        for i in range(len(pattern)):
            if pattern[i] not in d and word[i] in list(d.values()):
                return False
            if pattern[i] not in d:
                d[pattern[i]] = word[i]
            elif pattern[i] in d:
                if d[pattern[i]] == word[i]:
                    continue
                else:
                    return False
        return True
