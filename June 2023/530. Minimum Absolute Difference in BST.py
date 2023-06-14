# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        arr = []

        q = [root]

        while q:
            node = q.pop(0)
            arr.append(node.val)
    
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        arr.sort()
        output = float("inf")

        for i in range(len(arr)-1):
            output = min((arr[i+1] - arr[i]),output)
        
        return output
