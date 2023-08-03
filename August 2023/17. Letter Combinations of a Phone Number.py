class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        n = len(digits)
        if n == 0:
            return []
        number = defaultdict(list)
        letter = 97
        for i in range(2,10):
            if i == 9 or i == 7:
                for j in range(4):
                    number[i].append(chr(letter))
                    letter +=1
            else:
                for j in range(3):
                    number[i].append(chr(letter))
                    letter +=1

        output = []
        def back(S,k):
            if len(S) == n:
                output.append(S)
                return
            x = digits[k]
            for i in number[int(x)]:
                back(S+i,k+1)
            
            return
        
        back("",0)

        return output
