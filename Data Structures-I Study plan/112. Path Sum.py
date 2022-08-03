# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
                return None
            
        currsum = root.val
        def dfs(node,currsum):
            if node is None:
                return None
            currsum += node.val
          
            if currsum == targetSum and (node.left == None and node.right == None):
                return True
            
            
            return dfs(node.left,currsum) or dfs(node.right,currsum)
            
        
        if root.left != None and root.right != None:
            
            return dfs(root.left,currsum) or dfs(root.right,currsum)
        
        else:
            return dfs(root,currsum - root.val)
