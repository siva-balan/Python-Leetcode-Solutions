class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        '''m = len(s)
        n = len(t)
        
        if n > m :
            return ""
        
        l,r = 0,0
        d1 = Counter(t)
        d2 = {}
        output = float("inf")
        ans = ""
        while r < m or l <m:
            if r == m and len(d2) != len(d1):
                break
            elif len(d2) == len(d1):
                for i in d1:
                    if d1[i]> d2[i]:
                        if s[r] in d1:
                            d2[s[r]] = d2.get(s[r],0) +1
                        r +=1
                        break
                output = min(output,r-l+1)
                if output == r-l+1:
                    ans = s[l:r]
                if s[l] in d2:
                    d2[s[l]] -=1
                    if d2[s[l]] == 0:
                        del d2[s[l]]
                
                l +=1
            
            elif d2 != d1:
                if s[r] in d1:
                    d2[s[r]] = d2.get(s[r],0)+1
                r +=1
        return ans'''
        
        
        ############
        # FEW TESTCASES FAILS IN THE COMMENTED CODE ABOVE
        ############
        
        
        def t_is_in_substr(count_s: Counter, count_t: Counter) -> bool:            
            for char in count_t:
                if count_s[char] < count_t[char]:
                    return False
            return True
        
        m = len(s)
        n = len(t)

        count_s = Counter(s)
        count_t = Counter(t)
        

        if not t_is_in_substr(count_s, count_t):
            return ''

        count_s = Counter(s[0:1])
        left = 0
        right = 0
        
        curr = (m, s)

        while m - left >= n and right < m - 1:
            while not t_is_in_substr(count_s, count_t) and right < m - 1:
                right += 1
                count_s[s[right]] += 1
 
            while t_is_in_substr(count_s, count_t):
                count_s[s[left]] -= 1
                left += 1
                   
            if right - left + 1 < curr[0]:
                curr = (right - left + 1, s[left - 1:right + 1])
            
        return curr[1]
