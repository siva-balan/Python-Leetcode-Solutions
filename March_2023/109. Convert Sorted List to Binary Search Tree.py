# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        nums = []

        while head:
            nums.append(head.val)
            head = head.next
        
        def binarytree(nums):
            if not nums:
                return None
            mid = nums[(len(nums)//2)]
            root = TreeNode(mid)

            root.left = binarytree(nums[:len(nums)//2])
            root.right = binarytree(nums[len(nums)//2+1:])

            return root
        return binarytree(nums)
