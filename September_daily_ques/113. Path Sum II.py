# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        output = []
    
        def path(node,value,currsum,output):
            if node is None:
                return
            value.append(node.val)
            if node.left is None and node.right is None and currsum + node.val == targetSum:
                output.append(list(value))
            
            path(node.left,value,currsum+node.val,output)
            path(node.right,value,currsum+node.val,output)
            value.pop()
            
        path(root,[],0,output)
        
        return output
