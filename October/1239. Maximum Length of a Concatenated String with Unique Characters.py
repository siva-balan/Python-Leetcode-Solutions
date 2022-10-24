class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        n = len(arr)
        self.output = 0
        
        def unique(i,array,s):
            if len(s) == len(set(s)):
                self.output = max(self.output,len(s))
                for j in range(i,len(array)):
                    unique(j+1,array,s+array[j])
            else:
                return
        
        for i in range(len(arr)):
            unique(i+1,arr,arr[i])
        return self.output
