class Solution:
    def addDigits(self, num: int) -> int:

        output = 0

        for i in str(num):
            output+= int(i)
        
        while len(str(output)) >1:
            x = output
            output = 0
            for i in str(x):
                output += int(i)

        return output
