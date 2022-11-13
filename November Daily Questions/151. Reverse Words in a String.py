class Solution:
    def reverseWords(self, s: str) -> str:

        arr = s.split(" ")
        output = ""
        i = 0
        while i != len(arr):
            if arr[i] == "":
                arr.remove('')
            else:
                i+=1
        x = arr[::-1]

        for i in range(len(x)):
            output += x[i]
            if i == len(x)-1:
                break
            output += " "
        return output
