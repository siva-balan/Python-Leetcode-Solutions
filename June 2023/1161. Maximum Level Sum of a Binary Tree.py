# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        output,maxsum = 0, float("-inf")

        q = [root]
        level = 0
        while q:
            n = len(q)
            level +=1
            curr_sum = 0
            for i in range(n):
                node = q.pop(0)
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if curr_sum >maxsum:
                maxsum = curr_sum
                output = level
        
        return output
