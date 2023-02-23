class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort(key = lambda x : (x[0],-x[1]) )
        
        priq = []
        i = 0

        for m in range(k):
            while i < len(profits) and projects[i][0] <= w:
                heapq.heappush(priq,-projects[i][1]) # get all the projects with less capital and push it into heap
                i += 1
            if not priq:
                break
            x= heapq.heappop(priq) # pop the project with highest profit and add the profit to current capital
            w -=x
        
        return w
