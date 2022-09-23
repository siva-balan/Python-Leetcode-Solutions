
# DATE : 7/9/22

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        
        def bst(node):
            if not node:
                return
            if node.left and node.right:
                return str(node.val) + "(" + bst(node.left)+ ")" + "(" + bst(node.right)+")"
            elif node.left and node.right == None:
                return str(node.val) + "(" + bst(node.left) + ")"
            elif node.right and node.left ==None:
                return str(node.val) + "()" + "(" + bst(node.right)+ ")"
            else:
                return str(node.val)

        return bst(root)
