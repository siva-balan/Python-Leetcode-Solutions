class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:


        #Understoof from prog with larry/youtube

        d = defaultdict(int)

        for x in arr:
            if x - difference in d:
                d[x]= max(d[x-difference] +1,d[x])
            else:
                d[x] =1
        
        return max(d.values())
