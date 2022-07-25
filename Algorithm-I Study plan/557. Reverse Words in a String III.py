class Solution:
    def reverseWords(self, s: str) -> str:
        s= s.split(" ")
        rev = ''
        for i in range(len(s)):
            if i == len(s) -1:
                rev += s[i][::-1] 
            else:
                rev += s[i][::-1]+ ' ' 
        return rev
