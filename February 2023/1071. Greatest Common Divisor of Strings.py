class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        """output = ""
        n = len(str1) is len(str1) < len(str2) else len(str2)
        for i in range(n):
            if str1[i] == str2[i]:
                output += str1[i]
                for j in range(0,len(str1),len(output)):
                    if str1[j:len(output)+j] != output:
                        break"""
        
        if ( str1 + str2 ) != ( str2 + str1 ):			
            return ''
        else:
            length_by_gcd = gcd( len(str1), len(str2) )
            return str1[:length_by_gcd]
