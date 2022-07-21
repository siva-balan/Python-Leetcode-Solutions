class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        if x == 0:
            return 0
        if x<0:
            sign =-1
            y = str(x)
            y = y[1:]
            y = y[::-1]
            y = int(y.lstrip("0"))
        else:
            sign =1
            y = str(x)
            y = y[::-1]
            y = int(y.lstrip("0"))
        y = sign*y
        if y < -2**31 or y > (2**31)-1:
            return 0
        else:
            return y
