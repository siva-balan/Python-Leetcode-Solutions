class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        d = collections.Counter(nums)
        
        v = list(d.values())
        k = list(d.keys())
        
        x = k[v.index(max(v))]
        return x
