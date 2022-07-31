# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        itr = itr1 = head
        
        if itr == None:
            return itr
        while itr.next:
            if head == None:
                return head
            if head.val == val:
                head = head.next
                itr1 = head
                continue
            if itr.next.val == val and itr.next.next !=None:
                itr.next = itr.next.next
            elif itr.next.val == val and itr.next.next == None:
                itr.next = None
            else:
                itr = itr.next
                
        if itr.val == val:
            itr1 = itr.next
        return itr1
