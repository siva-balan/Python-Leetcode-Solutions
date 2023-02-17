# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        """q = [root]
        output = float("inf")
        while q:
            node = q.pop()
            if node.left:
                output = min(output,abs(node.val - node.left.val))
                q.append(node.left)
            if node.right:
                output = min(output,abs(node.val - node.right.val))
                q.append(node.right)
        
        return output"""

        arr = []
        q = [root]
        output = float("inf")
        while q:
            node = q.pop()
            arr.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        arr.sort()
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i]) < output:
                output = abs(arr[i+1]-arr[i])
        return output
