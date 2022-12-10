# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        self.totalSum=0
        self.res=0
        def findTotalSum(root):
            if not root: return 0
            findTotalSum(root.left)
            findTotalSum(root.right)
            self.totalSum+=root.val
        findTotalSum(root)
        def findSubTreeSum(root):
            if not root: return 0
            left=findSubTreeSum(root.left)
            right=findSubTreeSum(root.right)
            subTreeSum= left+right+root.val
            self.res=max(self.res,(self.totalSum-subTreeSum)*subTreeSum)
            return subTreeSum
        findSubTreeSum(root)
        return self.res%(10**9+7)
