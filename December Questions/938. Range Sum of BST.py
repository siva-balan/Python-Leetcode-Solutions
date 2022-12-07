# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        output = 0
        q = [root]

        while q:
            node = q.pop(0)
            if node.val >= low and node.val<=high:
                output += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return output
