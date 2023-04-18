class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        w1,w2 = list(word1) , list(word2)
        n1,n2 = len(w1),len(w2)
        
        i,j = 0,0
        output = ""

        while i < n1 or j < n2:
            if i == n1:
                output += "".join(w2[j:])
                j = n2
            elif j == n2:
                output += "".join(w1[i:])
                i = n1
            else:
                output += w1[i]
                i +=1
                output += w2[j]
                j +=1
        return output
