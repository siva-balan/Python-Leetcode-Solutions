# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        l = deque()
        l.append(root)
        
        while l:
            
            curr = l.popleft()
            if curr is not None:
                if curr.val == val :
                    return curr

                if curr.left and curr.right:
                    l.append(curr.left)
                    l.append(curr.right)
                elif curr.left is None:
                    l.append(curr.right)
                elif curr.right is None:
                    l.append(curr.left)
            
        return curr
