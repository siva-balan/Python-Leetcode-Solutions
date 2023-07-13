class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # d = defaultdict(list)

        # for x in prerequisites:
        #     d[x[0]].append(x[1])
        
        # for x in prerequisites:
        #     if x[0] in d[x[1]]:
        #         return False
        
        # return True

        pre = defaultdict(list)

        for course, p in prerequisites:
            pre[course].append(p)
        
        taken = set()

        def dfs(course):
            if not pre[course]:
                return True
            
            if course in taken:
                return False
            
            taken.add(course)

            for p in pre[course]:
                if not dfs(p):
                    return False
            
            pre[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
