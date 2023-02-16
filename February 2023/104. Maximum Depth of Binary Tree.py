# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        """def dfs(root):
            if root is None:
                return -1
            
            else:
                x = dfs(root.left)
                y = dfs(root.right)
                
                if x > y:
                    return x+1
                else:
                    return y+1
        
        ans =  1 + dfs(root)
        return ans"""

        def dfs(root,val):
            if root is None:
                return val
            else:
                x = dfs(root.left,val +1)
                y = dfs(root.right,val+1)

                if x > y:
                    return x
                else: return y
        
        return dfs(root,0)
            
