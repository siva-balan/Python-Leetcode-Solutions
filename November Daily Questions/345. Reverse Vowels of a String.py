class Solution:
    def reverseVowels(self, s: str) -> str:

        n = len(s)

        l,r = 0,n-1
        s = list(s)
        vowels = list("aeiouAEIOU")
        while l <r:
            while l<r and s[l] not in vowels:
                l +=1
            while r>l and s[r] not in vowels:
                r -=1
            s[l],s[r] = s[r],s[l]
            l +=1
            r-=1
        output = "".join(s)
        return output
