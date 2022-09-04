# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack1 = []
        stack2 = []
        stack1.append(p)
        stack2.append(q)
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        
        while stack1 and stack2:
            x = stack1.pop()
            y = stack2.pop()
            
            if x.val != y.val:
                return False
            if x.left is not None and y.left is not None:
                stack1.append(x.left)
                stack2.append(y.left)
            elif x.left is None and y.left is not None or x.left is not None and y.left is None:
                return False
            if x.right is not None and y.right is not None:
                stack1.append(x.right)
                stack2.append(y.right)
            elif x.right is None and y.right is not None or x.right is not None and y.right is None:
                return False
        return True
