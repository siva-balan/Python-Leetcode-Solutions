# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth ==1:
            return TreeNode(val,root)
        
        def dfs(node,curr_depth):
            if node:
                curr_depth +=1
                if curr_depth +1 == depth:
                    node.left = TreeNode(val,left = node.left)
                    node.right = TreeNode(val,right = node.right)
                dfs(node.left,curr_depth)
                dfs(node.right,curr_depth)
        dfs(root,0)
        
        return root
