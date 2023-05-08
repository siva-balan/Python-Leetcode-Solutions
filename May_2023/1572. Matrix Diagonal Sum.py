class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        output = 0
        r,c = len(mat),len(mat[0])
        for i in range(r):
            for j in range(c):
                # if r%2 == 0:
                if i == j or i+j == r -1:
                    output += mat[i][j]
                # else:
                #     if i== j and i == (r//2):
                #         print(mat[i][j])
                #         output += (mat[i][j])/2
                #     elif i == j or i+j == r -1:
                #         print(mat[i][j])
                #         output += mat[i][j]
        return int(output)
