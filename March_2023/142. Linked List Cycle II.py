# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}

        node = head
        while node:
            if node not in d:
                d[node] = 1
            else:
                return node
            node = node.next
        return None
