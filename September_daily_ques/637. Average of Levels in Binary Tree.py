
# DATE : 2/9/2022

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        output = []
        
        que = []
        que.append(root)
        
        while que:
            q =[]
            for i in range(len(que)):
                x = que.pop(0)
                q.append(x.val)
                que.append(x.left) if x.left else que
                que.append(x.right) if x.right else que
            ans = sum(q)/len(q)
            output.append(ans)
        return output
