class Solution:
    def longestPalindrome(self, s: str) -> str:
        result =''
        reslen = 0
        for i in range(len(s)):
            #even string
            l,r = i,i
            while l >=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    result = s[l:r+1]
                    reslen = r-l+1
                l -= 1
                r +=1
            
            #odd string
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    result = s[l:r+1]
                    reslen = r-l+1
                l -= 1
                r +=1
            
        return result
