class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 0: return ''
        if n == 1: return '1'
        
        s = '1'
        
        for _ in range(n-1):
            prev, count = s[0], 0
            newS = ''
			
            for l in s:
                if prev != l:
                    newS += str(count) + prev
                    prev, count = l, 1
                else: count += 1
					
            newS += str(count) + prev
            s = newS
        
        return s
