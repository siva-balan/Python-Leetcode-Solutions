class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        d = {}
        
        for i in sentence:
            if i not in d:
                d[i] =1
            else:
                d[i] +=1
        if len(d) == 26:
            return True
        else:
            return False
