class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = ['a','e','i','o','u']

        s = list(s)

        count = 0

        for i in range(len(s[:k])):
            if s[i] in vowels:
                count +=1
        output = count
        for j in range(k, len(s)):
            if s[j-k] in vowels:
                count -=1
            if s[j] in vowels:
                count +=1
            output = max(output,count)
        
        return output
