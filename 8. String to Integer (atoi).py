class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        sign = 1
        m =''
        if len(s) == 0:
            return 0
        if s[0] == '+':
            sign =1
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]
        for i in range(len(s)):
            if s[i].isdigit() != True:
                    break
            
            if s[i].isnumeric():
                
                m +=s[i]
        
        if len(m)==0:
            return 0
        result = sign*int(m)
        
        if result>(2**31)-1:
            return (2**31)-1
        elif result < -2**31:
            return (-2**31)
        else:
            return result
