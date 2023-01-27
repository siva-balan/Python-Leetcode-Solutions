class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        d = set(words)
        output = []
        def dfs(word):
            for i in range(1,len(word)):
                prefix = word[:i]
                suf = word[i:]
            
                if prefix in d and suf in d:
                    return True
                
                if prefix in d and dfs(suf):
                    return True
            return False
        for i in words:
            if dfs(i):
                output.append(i)
            
        return output
