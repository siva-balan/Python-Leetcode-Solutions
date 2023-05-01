class Solution:
    def average(self, salary: List[int]) -> float:

        n = len(salary)
        l = min(salary)
        r = max(salary)
        
        output = (sum(salary)-l-r)/(n-2)

        return output
