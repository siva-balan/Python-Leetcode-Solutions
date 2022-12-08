# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        leaf1 = []
        leaf2 = []

        s1,s2 = [root1],[root2]

        while s1:
            node = s1.pop()
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
            if not node.left and not node.right:
                leaf1.append(node.val)
        while s2:
            node = s2.pop()
            if node.left:
                s2.append(node.left)
            if node.right:
                s2.append(node.right)
            if not node.left and not node.right:
                leaf2.append(node.val)
        return leaf1 == leaf2
