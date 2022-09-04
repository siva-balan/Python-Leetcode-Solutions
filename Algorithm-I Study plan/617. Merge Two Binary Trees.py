# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2:
            return None
        if root1:
            x = root1.val  
        else: return root2
        if root2: 
            y = root2.val  
        else: return root1
        root = TreeNode(x + y) 

        root.left  = self.mergeTrees(root1.left ,root2.left)
        root.right = self.mergeTrees(root1.right,root2.right)
        
        return root
