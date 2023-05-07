class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        lis = []
        output = []
        for obstacle in obstacles:
            idx = bisect.bisect_right(lis, obstacle)
            if idx == len(lis):
                lis.append(obstacle)
            else:
                lis[idx] = obstacle
            output.append(idx+1)
        return output
