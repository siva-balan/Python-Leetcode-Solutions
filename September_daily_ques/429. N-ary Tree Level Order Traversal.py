
# DATE : 5/09/2022

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        output = []
        que = []
        que.append(root)
        
        if root is None:
            return output
        
        while que:
            q= []
            for i in range(len(que)):
                x = que.pop(0)
                q.append(x.val)
                for j in x.children:
                    que.append(j)
            output.append(q)
            
        return output
