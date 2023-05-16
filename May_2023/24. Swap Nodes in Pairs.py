# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        dummy = prev = ListNode()
        prev.next = head
        while prev.next and prev.next.next:
            t1 = prev.next
            t2 = prev.next.next
            t3 = prev.next.next.next

            prev.next = t2
            prev.next.next = t1
            prev.next.next.next = t3

            prev = t1
        
        return dummy.next


