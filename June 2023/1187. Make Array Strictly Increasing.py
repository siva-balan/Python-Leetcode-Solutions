class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        #Sol from leetcode


        arr2.sort()
        
        @cache
        def fn(i, prev): 
            """Return min ops to make arr1[i:] increasing w/ given previous element."""
            if i == len(arr1): return 0 
            ans = inf 
            if (prev < arr1[i]): ans = fn(i+1, arr1[i])
            k = bisect_right(arr2, prev)
            if k < len(arr2): ans = min(ans, 1 + fn(i+1, arr2[k]))
            return ans 
        
        ans = fn(0, -inf)
        return ans if ans < inf else -1
