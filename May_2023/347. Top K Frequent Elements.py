class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)

        freq = dict(sorted(freq.items(),key = lambda x :x[1],reverse = True))

        output = list(freq.keys())[:k]

        return output
