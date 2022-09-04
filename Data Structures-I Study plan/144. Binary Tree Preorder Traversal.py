# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        
        def preorder(root,l):
            if root == None:
                return root
            l.append(root.val)
            
            preorder(root.left,l)

            preorder(root.right,l)
        
        preorder(root,l)
        return l
