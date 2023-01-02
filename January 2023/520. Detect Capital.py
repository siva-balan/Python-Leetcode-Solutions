class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word[0].isupper():
            x = 0
            for i in range(1,len(word)):
                if word[i] .isupper():
                    x +=1
            if x == 0 or x == len(word) -1:
                return True
        else:
            x = 0
            for i in range(1,len(word)):
                if word[i] .isupper():
                    x +=1
            if x == 0:
                return True
        return False
