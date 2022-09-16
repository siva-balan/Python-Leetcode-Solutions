class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        res = []
        counter = defaultdict(int)

        changed.sort()
        for num in changed:
            if num % 2 == 0 and counter[num/2] > 0:
                counter[num/2] -= 1
                res.append(int(num/2))
            else:
                counter[num] += 1
        
        for val in counter.values():
            if val > 0:
                return []
        
        return res
