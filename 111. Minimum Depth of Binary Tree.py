# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        output = 0
        self.ans = 10**5
        def dfs(node,output):
            if node is None:
                return
            output +=1
            if node.left is None and node.right is None:
                self.ans = min(self.ans,output)
            else:
                dfs(node.left,output)
                dfs(node.right,output)
        dfs(root,output)
    
        return self.ans if self.ans != 10**5 else 0
            
