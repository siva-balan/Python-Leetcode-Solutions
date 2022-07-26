from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(0,numRows):
            temp = []
            for j in range(0,i+1):
                t = factorial(i)//(factorial(j)*factorial(i-j))
                temp.append(t)
            arr.append(temp)
        return arr
            
            
