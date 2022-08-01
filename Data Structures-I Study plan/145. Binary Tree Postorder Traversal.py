# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        
        def postorder(root,l):
            
            if root == None:
                return
            postorder(root.left,l)
            postorder(root.right,l)
            l.append(root.val)
        postorder(root,l)
        return l
