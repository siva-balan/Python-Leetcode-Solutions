class Solution:
    def compress(self, chars: List[str]) -> int:

        """n = len(chars)
        i = 0
        while i < len(chars):
            j = i+1
            count = 1
            while j < len(chars) and chars[j] == chars[i]:
                count +=1
                j +=1
            if count >1:
                chars[i+1:j] = list(str(count))
                i += len(str(count))
            else:
                i = j
        return len(chars)"""
        
        i,j = 0, 0
        while j < len(chars):
		
            chars[i] = chars[j]
            count = 1
			
            while j + 1 < len(chars) and chars[j] == chars[j+1]:
                j += 1
                count += 1
			
            if count > 1:
                for c in str(count):
                    chars[i+1] = c
                    i += 1
            
            j += 1
            i += 1
        
        return i
