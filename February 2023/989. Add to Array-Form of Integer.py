class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        for i in range(len(num)):
            num[i] = str(num[i])
        val = "".join(num)
        final_val = int(val) + k
        final_val = str(final_val)
        output = []
        for j in range(len(final_val)):
            output.append(int(final_val[j]))

        return output
