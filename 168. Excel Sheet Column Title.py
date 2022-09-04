class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
       
        x = columnNumber
        res = ""
        while x:
            res = chr((x-1)%26+65) + res
            x = (x-1)//26
        return res
