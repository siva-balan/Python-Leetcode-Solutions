class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0
        i=0
        while(i<len(s)):
            if i+1<len(s):
                if roman[s[i]] >= roman[s[i+1]]:
                    sum += roman[s[i]]
                    i+=1
                else:
                    sum += roman[s[i+1]] - roman[s[i]]              
                    i+=2
            else:
                sum= sum+ roman[s[i]]
                i+=1
        return sum
