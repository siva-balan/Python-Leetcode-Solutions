class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first, second = inf,inf
        
        for i in nums:
            if i < first:
                first = i
            elif first < i < second:
                second = i
            elif first < second < i:
                return True
        return False
