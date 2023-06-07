class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        output = 0

        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]
        n = max(len(a),len(b),len(c))

        if len(a) < n:
            a = "0"*(n-len(a)) + a
        if len(b) < n:
            b = "0"*(n-len(b)) + b
        if len(c) < n:
            c = "0"*(n-len(c)) + c

        for i in range(len(a)):
            if int(a[i]) | int(b[i]) == int(c[i]):
                continue
            elif int(c[i]) == 0:
                if int(a[i]) == 1 and int(b[i]) == 1:
                    output +=2
                else:
                    output +=1
            else:
                output +=1
        
        return output
