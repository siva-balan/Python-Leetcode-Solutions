# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        n = 0
        x = head
        while x:
            n +=1
            x = x.next
        if n <= 2:
            return head
        a = head
        b,c = head.next,head.next

        while a and b and b.next:
            a.next = b.next
            a = a.next
            if a:
                b.next = a.next
                b = b.next
        a.next = c

        return head
