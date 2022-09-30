# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        queue, d = deque([(root,0,0)]),defaultdict(list)
        
        output =[]
        
        while queue:
            for i in range(len(queue)):
                node,x,y = queue.popleft()
                
                d[y].append((abs(x),node.val))
                if node.left: queue.append((node.left,x+1,y-1))
                if node.right: queue.append((node.right,x+1,y+1))
        
        for i in sorted(d.keys()):
            output.append(x[1] for x in sorted(d[i]))
        return output
