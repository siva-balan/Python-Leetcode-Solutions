"""Intuition
To reach each node and add count to the total

Approach
Used Depth first search to visit each node and increase the count of node by 1 and return the total count

Complexity
Time complexity:
O(n)
Space complexity:
O(1), but technically O(n) as recursion uses in-built stack.
Code"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        output = [0]
        if root is None:
            return 0
        def dfs(node,output):
            if not node:
                return
            output[0] +=1
            dfs(node.left,output)
            dfs(node.right,output)

        dfs(root,output)
        return output[0]
