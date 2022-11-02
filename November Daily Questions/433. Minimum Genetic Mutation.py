class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        queue = deque([(start,0)])
        
        seen = {start}
        
        while queue:
            word,s = queue.popleft()
            
            if word == end:
                return s
            
            for i in "ACGT":
                for j in range(len(word)):
                    x = word[:j] + i + word[j+1:]
                    if x in bank and x not in seen:
                        queue.append((x,s+1))
                        seen.add(x)
        return -1
