class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    
        for char in letters:
            if ord(char) - ord(target) > 0:
                return char
        return letters[0]
        
