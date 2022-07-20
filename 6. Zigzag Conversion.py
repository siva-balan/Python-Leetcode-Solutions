class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ''
        if numRows ==1:
            return s
        for i in range(numRows):
            n = (numRows-1)*2
            for j in range(i,len(s),n):
                result +=s[j]
                if (i>0 and i<numRows-1 and j+n-2*i < len(s)):
                    result +=s[j+n-2*i]
            
        return result
