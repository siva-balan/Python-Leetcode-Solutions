# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        output = []

        def dfs(node,val):
            if node:
                val+= str(node.val)
            elif not node:
                return
            if node.left is None and node.right is None:
                output.append(val)
                return
            
            dfs(node.left,val)
            dfs(node.right,val)
            return
        dfs(root,"")
        
        total = 0
        for i in output:
            total+= int(i)
        
        return total
