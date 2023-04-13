class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        out = []
        i = 0
        j = 0
        while i < len(pushed):
            out.append(pushed[i])
            while out and j < len(popped) and out[-1] == popped[j]:
                out.pop()
                j +=1
            i +=1
        return j == len(popped)
        
