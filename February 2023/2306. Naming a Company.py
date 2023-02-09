class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        """output = 0
        d = {}
        for i in range(len(ideas)):
            for j in range(i+1,len(ideas)):
                a = ideas[i][0]+ideas[j][1:]
                b = ideas[j][0]+ideas[i][1:]
                print(a,b,"fwef")
                if a and b not in ideas:
                    print(ideas[i][0]+ideas[j][1:],ideas[j][0]+ideas[i][1:],"as")
                    x = ideas[i][0]+ideas[j][1:]+ " "+ ideas[j][0]+ideas[i][1:]
                    y = ideas[j][0]+ideas[i][1:]+ " "+ideas[i][0]+ideas[j][1:]
                    if x not in d:
                        d[x] = 1
                        output +=1
                        print(x)
                    if y not in d:
                        print(y)
                        d[y] =1
                        output +=1
        return output"""

        d = defaultdict(set)
        for w in ideas:
            d[w[0]].add(w[1:])
        
        output = 0
        for char1 in d:
            for char2 in d:
                if char1 == char2:
                    continue
                intersect = 0

                for w in d[char1]:
                    if w in d[char2]:
                        intersect += 1
                
                distinct1 = len(d[char1]) - intersect
                distinct2 = len(d[char2]) - intersect

                output += distinct1*distinct2
        return output
