# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        frequency = {}
        result = []
        self.findDuplicates(root, frequency, result)
        return result
    
    def findDuplicates(self, node, frequency, result):
        if node is None:
            return "#"
        
        subtree = str(node.val) + "," + self.findDuplicates(node.left, frequency, result) + "," + self.findDuplicates(node.right, frequency, result)
        frequency[subtree] = frequency.get(subtree, 0) + 1
        
        if frequency[subtree] == 2:
            result.append(node)
        
        return subtree
