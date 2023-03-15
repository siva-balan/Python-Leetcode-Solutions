# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        q = deque([root])

        while q[0] is not None:
            node = q.popleft()
            q.append(node.left)
            q.append(node.right)
        
        i = 0
        while i < len(q) and q[0] is None:
            q.popleft()
        
        return len(q) == 0
