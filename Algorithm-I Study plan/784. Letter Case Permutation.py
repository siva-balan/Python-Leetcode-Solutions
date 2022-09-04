class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        l = []
        def back(left,word):
            if left == len(word):
                l.append(word)
                return
            
            if word[left].isalpha():
                
                W = word[:left] + word[left].lower() + word[left+1:]
                back(left+1,W)
                
                W = word[:left] + word[left].upper() + word[left+1:]
                back(left+1,W)
            else:
                back(left+1,word)
        back(0,s)
        return l
