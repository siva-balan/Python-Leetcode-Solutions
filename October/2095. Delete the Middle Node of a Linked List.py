# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        root = head
        
        n = 0
        while root:
            n +=1
            root = root.next
        x= 0
        curr =head
        while curr:
            x +=1
            if x == n//2:
                curr.next = curr.next.next
                return head
            curr = curr.next
