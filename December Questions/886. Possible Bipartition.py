class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        """g1 = set()
        g2 = set()

        for d in dislikes:
            if d[0] and d[1] not in g1 or g2:
                g1.add(d[0])
                g2.add(d[1])
            if d[0] in g1 and d[1] not in g1:
                g2.add(d[1])
            elif d[0] in g2 and d[1] not in g2:
                g1.add(d[1])
            if d[1] in g1 and d[0] not in g1:
                g2.add(d[0])
            elif d[1] in g2 and d[0] not in g2:
                g1.add(d[0])
            
        if len(g1) + len(g2) != n:
            print(g1,g2)
            return False
        return True"""

        dislike_dict = {}
        for dislike in dislikes:
            if dislike[0] not in dislike_dict:
                dislike_dict[dislike[0]] = []
            if dislike[1] not in dislike_dict:
                dislike_dict[dislike[1]] = []
            dislike_dict[dislike[0]].append(dislike[1])
            dislike_dict[dislike[1]].append(dislike[0])
        
        group_dict = {}
        queue = []
        
        for i in range(1, n+1):
            if i not in group_dict:
                queue.append(i)
                group_dict[i] = 0
            while queue:
                person = queue.pop(0)
                group = group_dict[person]
                dislikes = dislike_dict.get(person, [])
                opposite_group = 1 - group
                for dislike in dislikes:
                    if dislike not in group_dict:
                        group_dict[dislike] = opposite_group
                        queue.append(dislike)
                    elif group_dict[dislike] == group:
                        return False
        return True
