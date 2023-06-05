class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        n = len(coordinates)
        if (coordinates[1][0] -coordinates[0][0]) == 0:
            slope = float("inf")
        else:
            slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] -coordinates[0][0])

        for i in range(1,n-1):
            if (coordinates[i+1][0] -coordinates[i][0]) == 0:
                if slope == float("inf"):
                    continue
                else:
                    return False
            if (coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] -coordinates[i][0]) == slope:
                continue
            else:
                return False

        return True 
