class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        plants = sorted(range(len(plantTime)),key = lambda x: growTime[x],reverse = True)
        curr =0
        output = 0
        for p in plants:
            curr += plantTime[p]
            output = max(output,curr+growTime[p])
        return output
