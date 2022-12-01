class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        s=s.lower()
        s1,s2 = "",""
        for i in range(len(s)//2):
            s1 += s[i]
            s2 += s[(len(s)//2)+i]
        
        vowels = ['a','e','i','o','u']
        c1,c2 = 0,0
        for i in vowels:
            c1 += s1.count(i)
            c2 += s2.count(i)
        if c1 == c2:
            return True
        else:
            return False
