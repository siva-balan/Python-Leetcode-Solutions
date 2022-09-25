class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        if len(words) == 0:
            return []
    
        i = 1
        
        while i < len(words):
            if "".join(sorted(words[i])) == "".join(sorted(words[i-1])):
                words.remove(words[i])
            else:
                i +=1
        return words
