class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) <=2 :
            return len(points)
        
        output = 0
        for i in list(combinations(points,2)):
                cnt = 0
                for j in points:
                    if (j[1] - i[0][1]) * (i[1][0] - i[0][0]) == (j[0] - i[0][0]) * (i[1][1] - i[0][1]):
                        cnt += 1
                output = max(output, cnt)
        return output
