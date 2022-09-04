# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        x = root
        
        if root is None:
            node = TreeNode(val)
            root = node
            return root
        
        if root.val < val and root.right is not None:
            self.insertIntoBST(root.right,val)
        elif root.val > val and root.left is not None:
            self.insertIntoBST(root.left,val)
        
        if root.val < val and root.right is None:
            node = TreeNode(val)
            root.right = node
        elif root.val > val and root.left is None:
            node = TreeNode(val)
            root.left = node
        
        return x
