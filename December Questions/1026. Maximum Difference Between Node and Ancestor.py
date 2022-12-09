# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        if not root : return 0

        st = [(root,root.val,root.val)] #node,parent,child
        output = 0
        while st:
            node, par, chi = st.pop()
            output = max(output,abs(par-chi))
            if node.left:
                st.append((node.left,max(par,node.left.val),min(chi,node.left.val)))
            if node.right:
                st.append((node.right,max(par,node.right.val),min(chi,node.right.val)))
        return output
