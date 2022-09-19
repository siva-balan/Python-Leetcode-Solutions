class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        
        d = defaultdict(list)
        
        for path in paths:
            path = path.split(" ")
            folder = path[0]
            
            for i in path[1:]:
                s = i.split(".txt")
                name = s[0]
                val = s[1]
                d[val].append((folder,name))
        output =[]
        
        for k,v in d.items():
            if len(v) >1:
                temp = []
                for p,n in v:
                    temp.append(p+'/'+n+'.txt')
                output.append(temp)
        return output
