class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def pal(w,st,end):
            while st<end:
                if w[st] != w[end]:
                    return False
                st +=1
                end -=1
            return True
        
        output = []
        n = len(words)
        
        d ={w:i for i,w in enumerate(words)}
        
        for i in range(n):
            w = words[i]
            if w == "":
                for j in range(n):
                    if i != j and pal(words[j],0,len(words[j])-1):
                        output.append([i,j])
                        output.append([j,i])
                continue
            rev = w[::-1]
            if rev in d and d[rev]!=i:
                output.append([i,d[rev]])
            
            for k in range(1,len(w)):
                for m in range(2):
                    bwj, l, r = (rev[k:], 0, k - 1) if m else (rev[:k], k, len(w) - 1)

                    if bwj in d and pal(rev, l, r):
                            output += [[i, d[bwj]]] if m else [[d[bwj], i]]
                
                
                '''if pal(w,0,k-1) and w[k:][::-1] in d:
                    output.append([d[w[k:][::-1]],i])
                if pal(w,k,len(w)-1) and w[:k][::-1] in d:
                    output.append([i,d[w[:k][::-1]]])'''
        return output
                    
