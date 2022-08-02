# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = deque()
        if root == None:
            return root
        l.append(root)
        output = []
        
        while len(l) != 0:
            x = len(l)
            y = []
            
            for i in range(x):
                curr = l.popleft()
                if curr.left != None:
                    l.append(curr.left)
                if curr.right != None:
                    l.append(curr.right)
                y.append(curr.val)
            output.append(y)
        
        return output
