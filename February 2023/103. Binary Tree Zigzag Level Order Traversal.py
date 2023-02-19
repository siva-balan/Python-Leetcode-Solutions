# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = [root]
        rev = False

        output = [[root.val]] if root else []
        if not root:
            return []
        while q:
            x = []
            y = len(q)
            for i in range(y):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    x.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    x.append(node.right.val)
            if rev == False:
                rev = True
                x= x[::-1]
                if len(x)>0:
                    output.append(x)
            else:
                rev = False
                if len(x)>0:
                    output.append(x)
             
        return output
