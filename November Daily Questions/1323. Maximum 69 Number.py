class Solution:
    def maximum69Number (self, num: int) -> int:

        x = list(str(num))
        print(x)
        for i in range(len(x)):
            if x[i] == '6':
                x[i] = '9'

                break
        return int("".join(x))
